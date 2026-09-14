# -*- coding: utf-8 -*-
"""
Google Stitch MCP Client
Provides direct programmatic access to Google Stitch design tools via MCP JSON-RPC.
"""

import urllib.request
import json
import os
from typing import Dict, Any, Optional, List

def get_stitch_api_key() -> str:
    """Retrieve Stitch API key from environment or global MCP config file."""
    if os.environ.get("STITCH_API_KEY"):
        return os.environ["STITCH_API_KEY"]
    mcp_config_path = os.path.expanduser(r"~\.gemini\config\mcp_config.json")
    if os.path.exists(mcp_config_path):
        try:
            with open(mcp_config_path, "r", encoding="utf-8") as f:
                cfg = json.load(f)
                headers = cfg.get("mcpServers", {}).get("stitch", {}).get("headers", {})
                return headers.get("X-Goog-Api-Key", "")
        except Exception:
            pass
    return ""

class StitchMCPClient:
    def __init__(self, api_key: Optional[str] = None, endpoint: str = STITCH_ENDPOINT):
        self.api_key = api_key or get_stitch_api_key()
        self.endpoint = endpoint
        self._request_id = 1

    def _call_rpc(self, method: str, params: Dict[str, Any]) -> Dict[str, Any]:
        payload = {
            "jsonrpc": "2.0",
            "id": self._request_id,
            "method": method,
            "params": params
        }
        self._request_id += 1

        headers = {
            "X-Goog-Api-Key": self.api_key,
            "Content-Type": "application/json"
        }

        req = urllib.request.Request(
            self.endpoint,
            data=json.dumps(payload).encode("utf-8"),
            headers=headers
        )

        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            if "error" in data:
                raise RuntimeError(f"Stitch MCP Error: {data['error']}")
            return data.get("result", {})

    def call_tool(self, tool_name: str, arguments: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Calls a specific MCP tool by name."""
        res = self._call_rpc("tools/call", {
            "name": tool_name,
            "arguments": arguments or {}
        })
        return res

    def list_tools(self) -> List[Dict[str, Any]]:
        """Lists all tools available on the Stitch MCP server."""
        res = self._call_rpc("tools/list", {})
        return res.get("tools", [])

    def list_projects(self) -> Dict[str, Any]:
        """Lists all accessible Stitch projects."""
        return self.call_tool("list_projects", {})

    def create_project(self, title: str) -> Dict[str, Any]:
        """Creates a new Stitch project container."""
        return self.call_tool("create_project", {"title": title})

    def list_screens(self, project_name: str) -> Dict[str, Any]:
        """Lists all screens inside a project."""
        return self.call_tool("list_screens", {"name": project_name})

    def get_screen(self, screen_name: str) -> Dict[str, Any]:
        """Retrieves details (HTML/CSS, layout) of a screen."""
        return self.call_tool("get_screen", {"name": screen_name})

    def generate_screen_from_text(self, project_name: str, prompt: str, screen_name: Optional[str] = None) -> Dict[str, Any]:
        """Generates a new screen in a project from a text prompt."""
        args = {
            "parent": project_name,
            "prompt": prompt
        }
        if screen_name:
            args["screenName"] = screen_name
        return self.call_tool("generate_screen_from_text", args)

    def list_design_systems(self, project_name: str) -> Dict[str, Any]:
        """Lists design systems for a given project."""
        return self.call_tool("list_design_systems", {"parent": project_name})

if __name__ == "__main__":
    client = StitchMCPClient()
    print("Testing Stitch MCP Client...")
    tools = client.list_tools()
    print(f"Connected successfully! {len(tools)} tools available.")
    projects = client.list_projects()
    print("Projects:", projects)

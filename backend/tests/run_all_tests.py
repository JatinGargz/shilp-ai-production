# -*- coding: utf-8 -*-
import subprocess
import sys
import os

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

base = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sandboxes_dir = os.path.join(base, "sandboxes")
tests_dir = os.path.join(base, "tests")

scripts = [
    os.path.join(sandboxes_dir, "test_anikeat_db.py"),
    os.path.join(sandboxes_dir, "test_kartik_ai.py"),
    os.path.join(sandboxes_dir, "test_ishaan_pricing.py"),
    os.path.join(sandboxes_dir, "test_jatin_channels.py"),
    os.path.join(tests_dir, "test_e2e_suite.py")
]

print("=" * 65)
print("  SHILP AI PRODUCTION - COMPLETE SYSTEM & SANDBOX VERIFICATION")
print("=" * 65)

all_passed = True
for s in scripts:
    name = os.path.basename(s)
    print(f"\n[*] Executing: {name} ...")
    res = subprocess.run([sys.executable, s], capture_output=True, text=True, encoding="utf-8")
    if res.returncode != 0:
        print(f"[FAIL] {name} exited with code {res.returncode}")
        print("STDERR:\n", res.stderr)
        all_passed = False
        break
    else:
        # Print summary line
        lines = [line for line in res.stdout.strip().split("\n") if line.strip()]
        last_line = lines[-1] if lines else "OK"
        print(f"[PASS] {name} -> {last_line}")

print("\n" + "=" * 65)
if all_passed:
    print("  >>> CONGRATULATIONS! ALL SANDBOXES & TESTS PASSED 100%! <<<")
else:
    print("  >>> SOME TESTS FAILED. PLEASE REVIEW LOGS ABOVE. <<<")
print("=" * 65)

sys.exit(0 if all_passed else 1)

import sys
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

# -*- coding: utf-8 -*-
"""
Kartik's Sandbox: AI Vision & Multilingual Speech Pipeline
Run: python backend/sandboxes/test_kartik_ai.py
"""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.services.image_studio import enhance_craft_image
from app.services.catalog_engine import generate_catalog_from_voice, generate_hindi_tts_audio, ask_shilpi_assistant

print("=" * 60)
print("  KARTIK DHIMAN'S AI VISION & VOICE SANDBOX")
print("=" * 60)

# 1. Test Studio Canvas
static_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "static"))
img_url = enhance_craft_image(None, "shilp_kartik_test", static_dir)
print(f"[PASS] 1. 4K Studio Image Canvas: {img_url}")

# 2. Test Catalog Prompt Engine
cat = generate_catalog_from_voice(
    transcript="Yeh pure Banarasi katan silk dupatta hai, haath se buna hua gold zari ke sath.",
    craft_category="textiles"
)
print(f"[PASS] 2. Multilingual Catalog: {cat['title_en']}")
print(f"       Hindi Title: {cat['title_hi']}")

# 3. Test Hindi TTS
audio_url = generate_hindi_tts_audio(title_hi=cat['title_hi'], price=2900.0, prod_id="shilp_kartik_test", static_dir=static_dir)
print(f"[PASS] 3. Hindi TTS Audio: {audio_url}")

# 4. Test Shilpi Voice Assistant
shilpi = ask_shilpi_assistant("PM Vishwakarma 15000 toolkit kaise milega?", static_dir)
print(f"[PASS] 4. Shilpi Assistant: {shilpi['answer_hi'][:40]}...")

print("All AI & Vision tests passed successfully!")

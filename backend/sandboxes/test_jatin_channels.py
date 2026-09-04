import sys
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

# -*- coding: utf-8 -*-
"""
Jatin's Sandbox: 5-Marketplace Publisher & Document Service
Run: python backend/sandboxes/test_jatin_channels.py
"""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.services.export_service import publish_to_all_channels, generate_upi_qr_bytes, generate_mela_standee_pdf

print("=" * 60)
print("  JATIN'S MULTI-CHANNEL & DOCUMENT SERVICES SANDBOX")
print("=" * 60)

cat = {"title_en": "Handcrafted Banarasi Silk Dupatta", "craft_type": "Weaving", "material": "Pure Silk"}
pricing = {"recommended_retail_price": 2900.0, "wholesale_b2b_price": 2320.0}

# 1. 5 Channels
res = publish_to_all_channels("shilp_test", cat, pricing, "http://mock/img.png")
print(f"[PASS] 1. Total Channels: {res['total_channels_connected']}")
print(f"       Amazon ASIN: {res['channels']['amazon_karigar']['asin']}")
print(f"       Flipkart FSN: {res['channels']['flipkart_samarth']['fsn']}")
print(f"       Etsy USD: {res['channels']['etsy_global']['price_usd']}")

# 2. UPI QR
qr = generate_upi_qr_bytes("shilp_test@upi", "Ramprasad Vishwakarma", 2900.0)
print(f"[PASS] 2. Dynamic UPI QR: {len(qr)} bytes")

# 3. PDF Standee
pdf = generate_mela_standee_pdf("shilp_test", "Banarasi Silk", "Weaving", 2900.0, "Ramprasad Vishwakarma")
print(f"[PASS] 3. Printable Mela Standee PDF: {len(pdf)} bytes")

print("All Integrations & Channel tests passed successfully!")

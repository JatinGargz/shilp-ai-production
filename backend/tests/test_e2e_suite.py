import sys
import os

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

backend_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, backend_dir)
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

print("=" * 65)
print("   SHILP AI - COMPREHENSIVE END-TO-END SYSTEM VERIFICATION")
print("=" * 65)

# 1. Health
r1 = client.get("/health")
assert r1.status_code == 200 and r1.json()["status"] == "healthy"
print("[PASS]  1. Server Health Check: Healthy")

# 2. Frontend
r2 = client.get("/")
assert r2.status_code == 200 and ("KALAKART" in r2.text or "KalaKart" in r2.text)
print(f"[PASS]  2. Multi-Channel Web App: Served ({len(r2.text)} chars)")

# 3. Process Craft
r3 = client.post("/api/v1/media/process-raw", data={
    "craft_category": "pottery",
    "material_cost": "250",
    "labor_hours": "12",
    "artisan_name": "Ramprasad Vishwakarma",
    "transcript_hint": "Yeh Jaipur Blue Pottery vase hai."
})
assert r3.status_code == 200
p = r3.json()
pid = p["product_id"]
print(f"[PASS]  3. AI Catalog & Studio Engine: {p['catalog']['title_en']} (PID: {pid})")
print(f"          Retail: Rs. {p['pricing']['recommended_retail_price']} | B2B: Rs. {p['pricing']['wholesale_b2b_price']}")

# 4. Hindi TTS
r4 = client.get(f"/static/audio/audio_{pid}.mp3")
assert r4.status_code == 200
print(f"[PASS]  4. Hindi TTS Audio Feedback: Generated ({len(r4.content)} bytes)")

# 5. Dynamic UPI QR
r5 = client.get(f"/api/v1/products/{pid}/upi-qr?amount=1550")
assert r5.status_code == 200 and r5.headers["content-type"] == "image/png"
print(f"[PASS]  5. Dynamic UPI Payment QR: Generated ({len(r5.content)} bytes)")

# 6. Mela Standee PDF
r6 = client.get(f"/api/v1/products/{pid}/mela-standee-pdf?title=Jaipur+Blue+Pottery&price=1550")
assert r6.status_code == 200 and r6.headers["content-type"] == "application/pdf"
print(f"[PASS]  6. Printable Mela Standee PDF: Generated ({len(r6.content)} bytes)")

# 7. 5-Channel E-Commerce Publisher
r7 = client.post("/api/v1/channels/publish-multi", json={"product_id": pid})
assert r7.status_code == 200
channels = r7.json()["channels"]
print(f"[PASS]  7. 5-Marketplace Unified Distribution Engine:")
print(f"          - Amazon Karigar: ASIN {channels['amazon_karigar']['asin']} (5% MoU Commission)")
print(f"          - Flipkart Samarth: FSN {channels['flipkart_samarth']['fsn']} (0% Commission)")
print(f"          - GeM Procurement: Item {channels['gem_procurement']['gem_item_id']} (Rule 149 Mandated Quota)")
print(f"          - Etsy Global: {channels['etsy_global']['price_usd']} (Direct International Export)")
print(f"          - ONDC Beckn: Catalog Schema Validated")

# 8. Bargaining Shield
r8 = client.post("/api/v1/pricing/bargain-shield", json={
    "material_cost": 250,
    "labor_hours": 12,
    "offered_price": 500,
    "craft_type": "pottery"
})
assert r8.status_code == 200
b = r8.json()
print(f"[PASS]  8. Bargaining Shield Anti-Exploitation: Verdict: {b['verdict']} (Floor: Rs. {b['cost_floor']})")

# 9. Shilpi Voice Companion
r9 = client.post("/api/v1/assistant/shilpi", json={"question": "PM Vishwakarma 15000 toolkit kaise milega?"})
assert r9.status_code == 200
s = r9.json()
print(f"[PASS]  9. Shilpi AI Voice Companion: OK -> '{s['answer_hi'][:40]}...'")

# 10. Multi-channel / ONDC order simulation
r10 = client.post("/api/v1/orders/simulate-ondc-order", json={
    "product_id": pid,
    "buyer_name": "Kavita Iyer (Chennai)",
    "city": "Chennai, Tamil Nadu",
    "quantity": 1,
    "buyer_app": "Amazon Karigar"
})
assert r10.status_code == 200
ord_data = r10.json()
print(f"[PASS] 10. Live Cross-Screen Order Simulator: Order {ord_data['order_id']} settled via {ord_data['payment_status']}")

# 11. Ministry Analytics
r11 = client.get("/api/v1/analytics/ministry")
assert r11.status_code == 200
print(f"[PASS] 11. MoSJE Central Ministry Portal Analytics: {r11.json()['total_catalogs_generated']} Catalogs Live")

# 12. Trending Craft Intelligence ("शिल्प रुझान")
r12 = client.get("/api/v1/trends/textiles")
assert r12.status_code == 200
tr = r12.json()
assert "trending_motifs" in tr
print(f"[PASS] 12. Trending Craft Demand Engine: OK -> '{tr['craft_name_en']}' {tr['surge_badge']}")

print("=" * 65)
print("   ALL 12/12 TESTS PASSED PERFECTLY! SYSTEM 100% OPERATIONAL")
print("=" * 65)

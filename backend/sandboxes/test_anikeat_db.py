import sys
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

# -*- coding: utf-8 -*-
"""
Anikeat's Sandbox: Database & Models Verification
Run: python backend/sandboxes/test_anikeat_db.py
"""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.core.database import engine, SessionLocal, Base
from app.models.models import Artisan, Product, ProductPricing, ProductMedia, B2BEnquiry

Base.metadata.create_all(bind=engine)
db = SessionLocal()

print("=" * 60)
print("  ANIKEAT'S DATABASE & SCHEMA SANDBOX")
print("=" * 60)

# Verify tables exist
tables = list(Base.metadata.tables.keys())
print(f"[PASS] Detected Tables: {tables}")
assert "artisans" in tables and "products" in tables and "product_pricing" in tables

# Verify query / upsert
artisan = db.query(Artisan).filter(Artisan.id == "artisan_001").first()
if not artisan:
    artisan = Artisan(
        id="artisan_001",
        name="Ramprasad Vishwakarma",
        phone="+919876543210",
        state="Uttar Pradesh",
        cluster="Varanasi Silk Weavers",
        craft_type="Banarasi Silk Weaving",
        scheme_id="PM-UP-4210"
    )
    db.add(artisan)
    db.commit()
    print("[PASS] Created Master Artisan: Ramprasad Vishwakarma")
else:
    print(f"[PASS] Master Artisan Found: {artisan.name} ({artisan.cluster})")

db.close()
print("All DB tests passed successfully!")

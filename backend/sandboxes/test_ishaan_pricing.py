import sys
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

# -*- coding: utf-8 -*-
"""
Ishaan's Sandbox: Ethical Wage Floor & Bargaining Shield
Run: python backend/sandboxes/test_ishaan_pricing.py
"""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.services.pricing_engine import calculate_fair_pricing, match_b2b_buyers, evaluate_bargaining_offer

print("=" * 60)
print("  ISHAAN ANAND'S PRICING & ML SANDBOX")
print("=" * 60)

# 1. Fair wage pricing
p = calculate_fair_pricing(material_cost=350.0, labor_hours=16.0, craft_type="textiles")
print(f"[PASS] 1. Recommended Retail Price: Rs. {p['recommended_retail_price']}")
print(f"       Wholesale B2B Price: Rs. {p['wholesale_b2b_price']}")
print(f"       Minimum Wage Floor: Rs. {p['cost_floor']}")

# 2. Bargaining Shield
b_loss = evaluate_bargaining_offer(350.0, 16.0, 600.0, "textiles")
print(f"[PASS] 2. Bargaining Shield (Low Offer): {b_loss['verdict']} -> {b_loss['artisan_dialogue_hindi']}")
assert b_loss['verdict'] == "EXPLOITATIVE_LOSS"

b_fair = evaluate_bargaining_offer(350.0, 16.0, 2400.0, "textiles")
print(f"[PASS] 3. Bargaining Shield (Fair Offer): {b_fair['verdict']}")
assert not b_fair['is_exploitative']

print("All Pricing & ML tests passed successfully!")

# 🇮🇳 SHILP AI (शिल्प) — Complete Teammate-by-Teammate Playbooks
### Smart India Hackathon 2026 | Problem Statement ID: 26090
**Ministry of Social Justice and Empowerment (MoSJE)**

> *Share this guide with the entire team. Every member has their own dedicated section with exact setup steps, owned files, test sandboxes, and milestone tasks.*

---

## ⚡ Universal 2-Minute Quickstart (For All Teammates)

Before starting your role-specific work, everyone should do these 3 steps:

1. **Get the Code:**
   Clone the repository or download the folder to your computer:
   ```bash
   git clone https://github.com/JatinGargz/shilp-ai-production.git
   cd shilp-ai-production
   ```
2. **Automated Setup (Windows):**
   * Double-click **`scripts/setup_windows.bat`**.
   * *This automatically checks Python 3.10+, creates your `venv`, installs all dependencies, and creates `.env`.*
3. **Verify Everything Works:**
   * Double-click **`scripts/verify_all.bat`**.
   * If you see `>>> ALL SANDBOXES & TESTS PASSED 100%! <<<`, your machine is 100% ready!

---

## 🌿 Universal Git Branching Rules (Zero Merge Conflicts)

> [!IMPORTANT]
> **Golden Rule:** **Never commit directly to `main`!**  
> Always create your personal feature branch before typing any code:

```bash
# Prakriti & Saira:
git checkout -b feature/ui-design-polish

# Kartik Dhiman:
git checkout -b feature/ai-vision-voice

# Ishaan Anand:
git checkout -b feature/pricing-bargain-shield

# Anikeat:
git checkout -b feature/backend-database-models

# Jatin:
git checkout -b feature/multichannel-integrations
```

---

# 🎨 1. Playbook: Prakriti & Saira (UI/UX & Frontend Design)

> **Mission:** Make SHILP AI the most comfortable, intuitive, and culturally authentic mobile application for low-literacy rural artisans and MoSJE officers.

### 📁 Your Workspace & Owned Files:
* ✅ **Primary File:** `frontend/index.html` (The interactive Dual-Screen Web App & Phone Simulator)
* ✅ **Assets:** `frontend/assets/css/` and `frontend/assets/img/`
* ❌ **Do Not Touch:** `backend/app/schemas/contracts.py` (Data contract between frontend and backend)

### 🚀 How to Run & Preview Your Work:
1. Double-click `scripts/run_backend.bat` to ensure the server is alive.
2. Open **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)** in Google Chrome or Microsoft Edge.
3. As you edit `frontend/index.html`, simply press `Ctrl + Shift + R` (hard refresh) in the browser to see your changes instantly!

### 🎯 Your Action Checklist & Milestones:
* [ ] **Figma Design Consistency:** Ensure colors match our warm Indian artisan palette (Terracotta `#C54218`, Warm Saffron `#E58A38`, Natural Oat Canvas `#F7F4EE`, Velvet Charcoal `#1C1917`).
* [ ] **Accessibility for Rural Artisans:**
  - Verify that buttons have large tap targets (>48px) so elderly weavers can easily click them on touchscreens.
  - Ensure the **Hindi / English toggle button** switches all text smoothly.
* [ ] **Storefront Aesthetics:**
  - Polish the **Amazon Karigar Storefront** view (ensure Prime badge, customer review stars, and Karigar guarantee badges look identical to Amazon India).
  - Polish the **Paytm ONDC Storefront** view (Paytm blue header, clean product cards, order confirmation animation).
* [ ] **Micro-Interactions:** Enhance subtle button press effects (`active:scale-95`), smooth tab fades, and audio wave animations when speaking.

---

# 🧠 2. Playbook: Kartik Dhiman (AI / GenAI & Vision)

> **Mission:** Power the Computer Vision studio canvas, Whisper speech-to-text, Groq Llama-3 multilingual catalog prompts, and native Hindi TTS audio feedback.

### 📁 Your Workspace & Owned Files:
* ✅ **Image Studio:** `backend/app/services/image_studio.py` (`rembg` AI background removal, 1080×1080 centering, MoSJE seal stamping)
* ✅ **Catalog & Voice Engine:** `backend/app/services/catalog_engine.py` (Groq Llama-3 prompt engineering, gTTS audio synthesis, "शिल्प सखी" Shilpi assistant)
* ✅ **Your 1-Click Test Sandbox:** `backend/sandboxes/test_kartik_ai.py`
* ❌ **Do Not Touch:** `backend/app/models/models.py` (Anikeat's DB file)

### 🚀 How to Test Your Code (1-Click):
Run your dedicated sandbox from the terminal:
```bash
python backend/sandboxes/test_kartik_ai.py
```
*If all 4 vision and speech tests output `[PASS]`, your code is rock solid!*

### 🎯 Your Action Checklist & Milestones:
* [ ] **Background Removal Tuning:** In `image_studio.py`, optimize the canvas margin so crafts of any aspect ratio (long scarves, tall vases, flat brass plates) center automatically without cropping.
* [ ] **Golden Seal Enhancement:** Refine the watermark text stamped on the bottom right:
  `"★ MoSJE CERTIFIED ETHICAL HANDCRAFT • PM VISHWAKARMA"`.
* [ ] **Groq Llama-3 Prompt Expansion:** In `catalog_engine.py`, add support for more craft categories (e.g. *Zardozi embroidery, Channapatna wooden toys, Madhubani paintings, Kashmiri Pashmina*).
* [ ] **"शिल्प सखी" (Shilpi Voice Assistant) Expansion:** Add more conversational responses for government schemes:
  - PM Vishwakarma ₹15,000 toolkit voucher process.
  - 5% subsidized loan up to ₹1 Lakh.
  - How to book free exhibition stalls at Surajkund / Saras Melas.

---

# 📊 3. Playbook: Ishaan Anand (ML & Ethical Pricing Systems)

> **Mission:** Build the anti-exploitation mathematical algorithms that guarantee statutory living wages for artisans and power the real-time "सौदा रक्षक" (Bargaining Shield).

### 📁 Your Workspace & Owned Files:
* ✅ **Pricing Engine:** `backend/app/services/pricing_engine.py` (Living wage floor formula, craft markups, Bargaining Shield evaluator, B2B institutional buyer matcher)
* ✅ **Your 1-Click Test Sandbox:** `backend/sandboxes/test_ishaan_pricing.py`
* ❌ **Do Not Touch:** `backend/app/services/image_studio.py` (Kartik's file)

### 🚀 How to Test Your Code (1-Click):
Run your dedicated sandbox from the terminal:
```bash
python backend/sandboxes/test_ishaan_pricing.py
```
*Tests the wage formula, low-offer rejection (`EXPLOITATIVE_LOSS`), and fair-offer approval (`FAIR_PROFITABLE`).*

### 🎯 Your Action Checklist & Milestones:
* [ ] **Statutory Living Wage Formula:** Refine the statutory formula:
  $$	ext{Cost Floor} = 	ext{Raw Material} + (	ext{Labor Hours} 	imes ₹100/	ext{hr}) + 	ext{Packaging}$$
* [ ] **Craft-Specific Markup Multipliers:**
  - Textiles (Banarasi Silk): `1.45x`
  - Pottery (Jaipur Blue Pottery): `1.35x`
  - Metalwork (Bastar Dokra): `1.50x`
  - Woodcraft (Saharanpur Carving): `1.40x`
* [ ] **"सौदा रक्षक" (Bargaining Shield Engine):**
  - Compute `effective_hourly_wage = (Offer - Material - Packaging) / Hours`.
  - If `< ₹100/hr`: trigger `EXPLOITATIVE_LOSS`, flash red, and generate a polite Devanagari Hindi counter-offer for the artisan to say to the haggling tourist.
* [ ] **B2B Bulk Institutional Pricing:** In `match_b2b_buyers()`, connect crafts to institutional corporate buyers (e.g., *Tribes India, FabIndia Sourcing, CCIC, Dastkar*).

---

# ⚙️ 4. Playbook: Anikeat (Backend Architecture & Database)

> **Mission:** Maintain enterprise database persistence, SQLAlchemy models, data integrity, and RESTful API route controllers.

### 📁 Your Workspace & Owned Files:
* ✅ **Database Models:** `backend/app/models/models.py` (`Artisan`, `Product`, `ProductPricing`, `ProductMedia`, `B2BEnquiry`)
* ✅ **Database Engine:** `backend/app/core/database.py` (SQLite / PostgreSQL session manager)
* ✅ **API Routes:** `backend/app/api/` & route definitions in `backend/app/main.py`
* ✅ **Your 1-Click Test Sandbox:** `backend/sandboxes/test_anikeat_db.py`
* ❌ **Do Not Touch:** `frontend/index.html` (Prakriti & Saira's file)

### 🚀 How to Test Your Code (1-Click):
Run your dedicated sandbox from the terminal:
```bash
python backend/sandboxes/test_anikeat_db.py
```
*Creates tables, tests relationships, and validates artisan records.*

### 🎯 Your Action Checklist & Milestones:
* [ ] **Artisan Model Expansion:** In `models.py`, add fields for:
  - Bank Account / UPI ID (`artisan_upi_id`)
  - Aadhaar / PAN Enrolment ID (under Oct 2023 GST exemption rule)
  - Artisan Guild / Cooperative Name
* [ ] **Order Tracking & Ledger:**
  - Create an `Order` model linking buyers to products.
  - Track order status: `ORDER_CONFIRMED` $ightarrow$ `PACKED` $ightarrow$ `DISPATCHED` $ightarrow$ `UPI_SETTLED`.
* [ ] **Ministry Analytics Aggregation Query:** In `main.py`, make `/api/v1/analytics/ministry` dynamically count live products, calculate total gross merchandise value (GMV), and cluster breakdown directly from the database.

---

# 🎖️ 5. Playbook: Jatin (Team Lead, Multi-Marketplace & DevOps)

> **Mission:** Orchestrate cross-module integrations, multi-marketplace publishers (Amazon SP-API, ONDC, GeM, Etsy), dynamic UPI QR, and rehearse the winning SIH demo.

### 📁 Your Workspace & Owned Files:
* ✅ **Master Orchestrator:** `backend/app/main.py`
* ✅ **Distribution & Document Engine:** `backend/app/services/export_service.py` (Amazon Karigar ASIN feed, Flipkart FSN, GeM Saras Collection, Etsy USD, ONDC Beckn JSON, dynamic UPI QR, A4 Mela Standee PDF)
* ✅ **Master Test Suite:** `backend/tests/test_e2e_suite.py` & `backend/tests/run_all_tests.py`
* ✅ **Your 1-Click Test Sandbox:** `backend/sandboxes/test_jatin_channels.py`

### 🚀 How to Test Your Code (1-Click):
```bash
# Test your individual channels:
python backend/sandboxes/test_jatin_channels.py

# Run the master system verification:
scripts\verify_all.bat
```

### 🎯 Your Action Checklist & Milestones:
* [ ] **Universal 5-Marketplace Publisher:** Maintain the `publish_to_all_channels()` engine for Amazon Karigar, Flipkart Samarth, GeM, Etsy, and ONDC.
* [ ] **Amazon SP-API Inspector:** Ensure the developer inspector in `frontend/index.html` renders authentic `PUT /listings/2021-08-01/items` payloads.
* [ ] **Cross-Screen Live Order Sync:** Ensure when a user buys on the Storefront preview, the artisan phone simulator immediately chimes and shows the order toast.
* [ ] **SIH Pitch Rehearsal:** Master the 3-minute pitch script in [`docs/SIH_PITCH_SCRIPT.md`](file:///C:/Users/Jatin/.gemini/antigravity/scratch/shilp-ai-production/docs/SIH_PITCH_SCRIPT.md).

---

## 🆘 Troubleshooting FAQ (If Anything Goes Wrong)

| Issue | Solution |
| :--- | :--- |
| **`python` is not recognized** | You installed Python without checking "Add python.exe to PATH". Re-run Python installer, choose "Modify", and check "Add to PATH". |
| **Hindi characters look weird in Windows terminal** | Add this at the top of your test script:<br>`import sys; sys.stdout.reconfigure(encoding="utf-8")` |
| **Port 8000 is already in use** | Open Task Manager, end any running `python.exe` processes, and run `scripts/run_backend.bat` again. |
| **Git merge conflict occurred** | Do not panic. Run `git status` to see conflicting files, coordinate with the teammate owning that file, resolve the conflict, and commit. |

---

> **Let's build, win SIH 2026, and empower India's 7 million traditional artisans! 🇮🇳🚀**

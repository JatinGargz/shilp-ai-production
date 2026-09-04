# 🇮🇳 SHILP AI — Team Execution Masterplan & Milestone Roadmap
> **SIH 2026 Problem Statement ID:** 26090  
> **Target Ministry:** Ministry of Social Justice and Empowerment (MoSJE)  
> **Official Team Codebase:** `shilp-ai-production`

---

## 👥 Roles & Accountabilities Matrix

| Teammate | Official Role | Primary Modules & Code Files | Individual Sandbox |
| :--- | :--- | :--- | :--- |
| **Jatin** | **Team Lead & Integrations** | Master FastAPI router, Amazon SP-API, ONDC Beckn payloads, Mela Standee PDF, dynamic UPI QR | `backend/sandboxes/test_jatin_channels.py` |
| **Prakriti & Saira** | **UI/UX & Product Design** | Design system tokens, Figma wireframes, artisan mobile PWA usability, Amazon & Paytm storefront styling | `frontend/index.html` & `frontend/assets/css/` |
| **Anikeat** | **Backend & Database** | SQLAlchemy database schemas, SQLite migrations, CRUD endpoints, order settlement webhooks | `backend/sandboxes/test_anikeat_db.py` |
| **Kartik Dhiman** | **AI / GenAI & Vision** | `rembg` background removal, 1080p canvas centering, Whisper STT, Groq Llama-3.3 prompt tuning | `backend/sandboxes/test_kartik_ai.py` |
| **Ishaan Anand** | **ML & Pricing Systems** | Ethical minimum wage-floor algorithm, category profit markups, "सौदा रक्षक" Bargaining Shield | `backend/sandboxes/test_ishaan_pricing.py` |

---

## 📅 Hackathon Milestones & Sprint Schedule

### Phase 1: Environment & Sandbox Verification (Hour 0 - 2)
- [x] Every team member clones `shilp-ai-production`.
- [x] Windows teammates run `scripts/setup_windows.bat`.
- [x] Each member verifies their dedicated sandbox script:
  - Anikeat: `python backend/sandboxes/test_anikeat_db.py`
  - Kartik: `python backend/sandboxes/test_kartik_ai.py`
  - Ishaan: `python backend/sandboxes/test_ishaan_pricing.py`
  - Jatin: `python backend/sandboxes/test_jatin_channels.py`
- [x] Prakriti & Saira open `http://127.0.0.1:8000/` to test UI ergonomics.

### Phase 2: Domain Deep-Dives & Enhancements (Hour 2 - 12)
- **Prakriti & Saira:** Add visual flair to the mobile simulator, refine voice wave animations, and fine-tune typography for low-literacy artisans.
- **Anikeat:** Expand `models.py` with artisan bank account verification fields, GI-certificate registration IDs, and order tracking timestamps.
- **Kartik:** Enhance `catalog_engine.py` with multi-dialect support (Bhojpuri, Rajasthani, Chhattisgarhi craft prompts) and studio lighting presets.
- **Ishaan:** Expand `pricing_engine.py` with seasonal demand multipliers (e.g. Diwali festive spike, tourist mela inflation coefficients).
- **Jatin:** Connect the Amazon SP-API mock dispatcher with simulated webhook callbacks and finalize printable PDF standee aesthetics.

### Phase 3: Integration & Dry Run (Hour 12 - 20)
- Run `scripts/verify_all.bat` to confirm all 11 master tests pass seamlessly.
- Conduct simulated judge demo rounds using the 1-tap craft presets.
- Rehearse the 3-minute pitch script (`docs/SIH_PITCH_SCRIPT.md`).

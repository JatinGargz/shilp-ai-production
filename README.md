# 🇮🇳 SHILP AI (शिल्प) — Smart Handicraft Intelligence & Linkage Platform
### SIH 2026 Problem Statement ID: 26090 | Ministry of Social Justice and Empowerment (MoSJE)

> **Official Production Repository for Team SIH 2026.**  
> A Voice-First AI Virtual Business Manager & Multi-Marketplace Publisher empowering marginalized artisans (PM Vishwakarma & PM-DAKSH) to photograph, catalog, price ethically, and distribute Indian handicrafts across 5 major e-commerce platforms.

---

## ⚡ 1-Click Fast Start for Team Members

### 🪟 Windows Setup (Jatin, Prakriti, Saira, Anikeat, Kartik, Ishaan)
1. Double-click **`scripts/setup_windows.bat`**.
   *(Creates Python venv, installs all pinned packages, and sets up `.env`)*
2. Double-click **`scripts/run_backend.bat`**.
   *(Starts FastAPI server at `http://127.0.0.1:8000`)*
3. Open **`http://127.0.0.1:8000/`** in Chrome to interact with the live Dual-Screen booth!

### 🧪 Isolated Developer Sandboxes
Each teammate has their own zero-interference test sandbox:
* **Anikeat (Database & Models):** `python backend/sandboxes/test_anikeat_db.py`
* **Kartik (Vision & Speech):** `python backend/sandboxes/test_kartik_ai.py`
* **Ishaan (Pricing & Bargaining):** `python backend/sandboxes/test_ishaan_pricing.py`
* **Jatin (5-Channels & Documents):** `python backend/sandboxes/test_jatin_channels.py`

### 🛡️ Master System Verification (11/11 Passed)
```bash
scripts\verify_all.bat
```

---

## 👥 Team Roles & Responsibilities

| Role | Members | Core Focus |
| :--- | :--- | :--- |
| **Team Lead & Integrations** | **Jatin** | Multi-channel architecture, Amazon SP-API, ONDC Beckn schema, UPI QR, Mela Standee PDF |
| **UI/UX & Design** | **Prakriti & Saira** | Figma design tokens, comfortable warm palette, mobile simulator UX, Amazon & Paytm storefronts |
| **Backend & Database** | **Anikeat + Jatin** | FastAPI microservices, SQLAlchemy schemas, database migrations, and order settlement webhooks |
| **AI / GenAI & Vision** | **Kartik Dhiman** | `rembg` background removal, 1080p canvas centering, Whisper STT, and Groq Llama-3.3 engine |
| **ML & Pricing** | **Ishaan Anand** | Dynamic wage-floor pricing algorithm, craft category markups, and Bargaining Shield engine |

---

## 📁 Repository Map

```
shilp-ai-production/
├── docs/                        # Architecture, pitch script, masterplan
├── backend/
│   ├── app/
│   │   ├── core/database.py     # SQLAlchemy connection engine
│   │   ├── models/models.py     # Database tables (Artisan, Product, Pricing, Media)
│   │   ├── schemas/contracts.py # FROZEN DATA CONTRACTS (Pydantic v2)
│   │   ├── services/            # Vision, Voice, Pricing, 5-Marketplace, PDF generators
│   │   └── main.py              # FastAPI orchestrator
│   ├── sandboxes/               # Individual teammate test sandboxes
│   ├── tests/                   # Master 11-point E2E test suite
│   └── requirements.txt         # Pinned production dependencies
├── frontend/
│   └── index.html               # Comfy, smooth, multi-screen live booth
└── scripts/
    ├── setup_windows.bat        # 1-Click environment setup
    ├── run_backend.bat          # 1-Click backend server starter
    └── verify_all.bat           # 1-Click test runner
```

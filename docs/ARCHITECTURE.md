# 🏛️ SHILP AI System Architecture & Data Flow

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                                   ARTISAN CLIENT LAYER                                 │
│                                                                                        │
│   📱 Progressive Web App (PWA) / Dual-Screen Live Simulator                           │
│   ├── Live Web Camera Capture / File Upload                                            │
│   ├── Web Speech API Voice Recognition (Hindi/English)                                │
│   ├── "सौदा रक्षक" (Bargaining Shield Real-Time Calculator)                             │
│   ├── "शिल्प सखी" (Shilpi Voice Assistant Modal)                                       │
│   └── 1-Tap Craft Quick Presets (Banarasi Silk, Jaipur Pottery, Bastar Dokra)          │
└──────────────────────────────────────────┬─────────────────────────────────────────────┘
                                           │ HTTP Multi-Part Form
                                           ▼
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                              FASTAPI ORCHESTRATION GATEWAY                             │
│                                 (http://127.0.0.1:8000)                                │
│                                                                                        │
│   [POST /api/v1/media/process-raw]  [POST /api/v1/channels/publish-multi]              │
│   [POST /api/v1/pricing/bargain-shield] [POST /api/v1/assistant/shilpi]               │
└──────┬───────────────────────┬───────────────────────┬──────────────────────────┬──────┘
       │                       │                       │                          │
       ▼                       ▼                       ▼                          ▼
┌──────────────┐       ┌───────────────┐       ┌───────────────┐          ┌───────────────┐
│ VISION STUDIO│       │ VOICE CATALOG │       │ PRICING ENGINE│          │ 5-MARKETPLACE │
│ (`rembg` AI) │       │ (Groq Llama-3)│       │ (Wage Floor)  │          │ DISTRIBUTION  │
│ 1080p Canvas │       │ Multilingual  │       │ Anti-Bargain  │          │ Amazon ASIN   │
│ MoSJE Seal   │       │ gTTS Hindi    │       │ Shield Formula│          │ Flipkart FSN  │
└──────────────┘       └───────────────┘       └───────────────┘          │ GeM Quota     │
                                                                          │ Etsy USD ($)  │
                                                                          │ ONDC Beckn    │
                                                                          └───────────────┘
```

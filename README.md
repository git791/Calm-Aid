# 🩺 CalmAid — Emergency First Aid AI Agent

> Speak the emergency. Show the injury. Get calm, step-by-step instructions — live.

**Gemini Live Agent Challenge · Live Agents category**

---

## 🎯 What It Does

CalmAid is a multimodal AI first aid assistant. In an emergency, you:

1. **Speak** — describe the situation using your mic
2. **Show** — take a photo of the injury with your camera
3. **Hear** — CalmAid streams instructions back word-by-word and reads them aloud simultaneously

No typing. No waiting. Real-time voice + vision + streaming response.

---

## ✨ Features

- 🎙️ **Voice input** — Web Speech API, no setup required
- 👁️ **Vision** — Camera snap or image upload analyzed by Gemini
- ⚡ **Live streaming** — Response streams word-by-word via Server-Sent Events
- 🔊 **Auto TTS** — Speaks in sentence chunks as they arrive, not after
- 🛡️ **Safety-first** — System prompt enforces disclaimers and 911 escalation
- 🎨 **GSAP animations** — Staggered page load, response reveal, particle background

---

## 🏗️ Architecture

```
User (Chrome Browser)
    │
    ├── 🎙️ Web Speech API → text transcript
    ├── 📷 Camera / File Upload → base64 image
    │
    ▼
FastAPI Backend (Google Cloud Run)
    │
    ├── google-genai SDK
    │       └── Gemini 2.5 Flash
    │               ├── Vision (image analysis)
    │               └── Streaming (SSE chunks)
    │
    ├── Secret Manager (API key)
    │
    └── Static files (frontend/index.html)
         │
         └── Browser TTS (Web Speech Synthesis API)
```

**Google Cloud services used:**
- Cloud Run — serverless hosting
- Secret Manager — secure API key storage
- Cloud Build — container builds
- Artifact Registry — Docker image storage

---

## 🚀 Local Setup

### Prerequisites
- Python 3.11+
- Chrome browser
- Gemini API key → [aistudio.google.com](https://aistudio.google.com)

### Steps

```bash
# 1. Clone
git clone https://github.com/YOUR_USERNAME/calmaid-agent
cd calmaid-agent

# 2. Create and activate venv
python -m venv venv

# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set API key
# Windows
$env:GEMINI_API_KEY = "your-key-here"
# Mac/Linux
export GEMINI_API_KEY="your-key-here"

# 5. Run
uvicorn backend.main:app --reload --port 8080
```

Open **http://127.0.0.1:8080** in Chrome.

---

## ☁️ Deploy to Cloud Run

### Prerequisites
- [gcloud CLI](https://cloud.google.com/sdk/docs/install) installed and authenticated
- GCP project with billing enabled
- APIs enabled: Cloud Run, Cloud Build, Secret Manager

```bash
# 1. Authenticate
gcloud auth login
gcloud auth configure-docker

# 2. Edit deploy.sh — set your PROJECT_ID
# 3. Run
$env:GEMINI_API_KEY = "your-key-here"
bash scripts/deploy.sh
```

The script automatically:
- Stores API key in Secret Manager
- Builds Docker image via Cloud Build
- Deploys to Cloud Run with secret injected

---

## 📦 Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Vanilla HTML/CSS/JS + GSAP 3 |
| Voice Input | Web Speech API (browser-native) |
| Voice Output | Web Speech Synthesis API (browser-native) |
| Backend | FastAPI + Uvicorn |
| AI Model | Gemini 2.5 Flash (google-genai SDK) |
| Streaming | Server-Sent Events (SSE) |
| Hosting | Google Cloud Run |
| Secrets | Google Secret Manager |
| Container | Docker via Cloud Build |

---

## 🗂️ Project Structure

```
calmaid-agent/
├── backend/
│   └── main.py          # FastAPI app, SSE streaming endpoint
├── frontend/
│   └── index.html       # Full UI — HTML/CSS/JS/GSAP
├── scripts/
│   └── deploy.sh        # One-command Cloud Run deployment
├── Dockerfile           # Alpine-based Python container
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

## 🔐 Safety Design

- System prompt prohibits diagnosis or medication advice
- Every response ends with 911 escalation reminder
- Gemini safety filters active
- API key stored in Secret Manager, never hardcoded

---

## 🏆 Hackathon

- **Challenge:** Gemini Live Agent Challenge 2025
- **Category:** Live Agents 🗣️
- **Mandatory tech:** Google GenAI SDK, Google Cloud Run

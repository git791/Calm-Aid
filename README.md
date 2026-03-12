# 🩺 CalmAid – Emergency First Aid AI Agent

> Speak to describe an emergency. Show the injury. Get calm, step-by-step voice instructions instantly.

**Built for the Gemini Live Agent Challenge** · Live Agents category

---

## 🎯 What It Does

CalmAid is a multimodal AI first aid assistant that:
- 🎙️ **Hears you** — Uses your browser mic (Web Speech API) for real-time voice input
- 👁️ **Sees the injury** — Accepts a photo via camera or file upload, analyzed by Gemini Vision
- 🔊 **Speaks back** — Reads first aid instructions aloud using text-to-speech
- 🛡️ **Stays safe** — Built-in safety system prompt with disclaimers and 911 escalation

---

## 🏗️ Architecture

```
User (Browser)
    │
    ├── 🎙️ Web Speech API (mic → text transcript)
    ├── 📷 Camera / File Upload (image)
    │
    ▼
Streamlit App (Cloud Run · us-central1)
    │
    ├── google-generativeai SDK
    │       └── Gemini 1.5 Flash (vision + text)
    │
    ├── Secret Manager (API key storage)
    │
    └── gTTS (text → mp3 → autoplay in browser)
```

**Google Cloud Services used:**
- Cloud Run (hosting)
- Secret Manager (API key security)
- Cloud Build (container build)
- Artifact Registry (image storage)

---

## 🚀 Local Setup (Day 1 — ~15 mins)

### Prerequisites
- Python 3.11+
- A [Gemini API key](https://aistudio.google.com/app/apikey)

### Steps

```bash
# 1. Clone the repo
git clone https://github.com/YOUR_USERNAME/calmaid-agent
cd calmaid-agent

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set your API key
export GEMINI_API_KEY="your-key-here"

# 4. Run locally
streamlit run app.py
```

Open **http://localhost:8501** in Chrome (required for mic access).

---

## ☁️ Deploy to Cloud Run (Day 2 — ~20 mins)

### Prerequisites
- [gcloud CLI](https://cloud.google.com/sdk/docs/install) installed
- A GCP project with billing enabled
- APIs enabled: Cloud Run, Cloud Build, Secret Manager

```bash
# 1. Authenticate
gcloud auth login
gcloud auth configure-docker

# 2. Edit deploy.sh — set your PROJECT_ID
nano scripts/deploy.sh

# 3. Set your API key as env var
export GEMINI_API_KEY="your-key-here"

# 4. Run the deploy script
bash scripts/deploy.sh
```

The script will:
- Store your API key in Secret Manager (never hardcoded)
- Build the Docker image via Cloud Build
- Deploy to Cloud Run with the secret injected

---

## 🧪 How to Use

1. Open the app in **Chrome**
2. Click **🎙️ Start Speaking** and describe the emergency
3. Click **⏹ Stop**, then **📋 Copy transcript**
4. Paste the transcript in the text box
5. Optionally take a photo of the injury
6. Click **🚨 Get First Aid Help**
7. CalmAid reads instructions aloud automatically

---

## 🔐 Safety Design

- System prompt prohibits diagnosis
- Always escalates to 911 for serious emergencies
- Vertex AI safety filters active
- All responses capped at ~120 words for clarity under stress

---

## 📦 Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | Streamlit + Web Speech API |
| AI Model | Gemini 1.5 Flash (Google GenAI SDK) |
| Voice Out | gTTS (Google Text-to-Speech) |
| Hosting | Google Cloud Run |
| Secrets | Google Secret Manager |
| Container | Docker via Cloud Build |

---

## 🏆 Hackathon Submission

- **Category:** Live Agents 🗣️
- **Challenge:** Gemini Live Agent Challenge
- **Team:** [Your Name]
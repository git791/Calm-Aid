# CalmAid -- AI Emergency First Aid Assistant 🚑

CalmAid is an AI-powered emergency first aid assistant that provides
instant step‑by‑step guidance during emergencies using voice, text, and
image input.

The system analyzes the situation using Google Gemini AI, streams
responses in real time, and reads instructions aloud so users can act
quickly in critical situations.

⚠️ CalmAid provides general first aid guidance only and is not a
substitute for professional medical help.

------------------------------------------------------------------------

# Demo Overview

CalmAid allows users to:

-   Describe an emergency using voice or text
-   Upload or capture an image of the injury
-   Receive AI-generated first aid instructions instantly
-   See instructions stream in real time
-   Hear the instructions spoken aloud

------------------------------------------------------------------------

# Key Features

## 🎙 Voice Input

Uses the Web Speech API to convert speech into text for describing the
emergency.

## 📝 Text Input

Users can manually type the situation.

## 📷 Image Analysis

Users can upload or capture images of injuries to improve AI
understanding.

## ⚡ Real-Time Streaming AI

Responses are streamed from the AI model using Server-Sent Events (SSE).

## 🔊 Voice Instructions

Instructions are automatically spoken aloud using Text-to-Speech (TTS).

## 🎨 Interactive UI

Modern responsive interface with animations and live updates.

## 🐳 Docker Deployment

Runs fully inside a Docker container for simple deployment.

------------------------------------------------------------------------

# System Architecture

User → Frontend (Voice/Text/Image) → FastAPI Backend → Gemini AI →
Streaming Response → Frontend UI + Voice Output

Main components:

Frontend - HTML - CSS - JavaScript - Web Speech API - Camera API

Backend - FastAPI - Pillow - Google GenAI SDK

AI - Gemini 2.5 Flash

Infrastructure - Docker - Uvicorn

------------------------------------------------------------------------

# Project Structure

    CalmAid
    │
    ├── backend
    │   └── main.py
    │
    ├── frontend
    │   └── index.html
    │
    ├── requirements.txt
    │
    ├── Dockerfile
    │
    └── README.md

------------------------------------------------------------------------

# Installation

## 1. Clone the repository

    git clone https://github.com/YOUR_USERNAME/CalmAid.git
    cd CalmAid

## 2. Install dependencies

    pip install -r requirements.txt

## 3. Set environment variable

Linux / Mac

    export GEMINI_API_KEY=your_api_key_here

Windows

    set GEMINI_API_KEY=your_api_key_here

------------------------------------------------------------------------

# Run the Server

    uvicorn backend.main:app --host 0.0.0.0 --port 8080

Open in browser:

http://localhost:8080

------------------------------------------------------------------------

# Run with Docker

Build container:

    docker build -t calmaid .

Run container:

    docker run -p 8080:8080 -e GEMINI_API_KEY=your_api_key calmaid

Open:

http://localhost:8080

------------------------------------------------------------------------

# API Endpoint

## POST /api/aid/stream

Streams first aid instructions from the AI model.

Request:

``` json
{
  "text": "My friend burned their hand on a stove",
  "image_b64": "optional_base64_image"
}
```

Response (Server-Sent Events):

    data: {"chunk": "..."}
    data: {"chunk": "..."}
    data: {"done": true}

------------------------------------------------------------------------

# Technologies Used

  Technology        Purpose
  ----------------- ---------------------
  FastAPI           Backend API
  Google Gemini     AI reasoning
  Pillow            Image processing
  Web Speech API    Voice recognition
  SpeechSynthesis   Text-to-speech
  SSE               Real-time streaming
  Docker            Containerization
  Uvicorn           ASGI server

------------------------------------------------------------------------

# Safety Rules

The AI assistant:

-   Provides first aid guidance only
-   Does not diagnose medical conditions
-   Does not prescribe medication
-   Encourages users to call emergency services

Every response ends with:

"If this is a serious emergency, please call 911 immediately."

------------------------------------------------------------------------

# Future Improvements

-   Multilingual voice support
-   Offline first aid knowledge base
-   Medical image classification models
-   Emergency contact integration
-   Mobile application
-   Location-based emergency numbers

------------------------------------------------------------------------

# Disclaimer

CalmAid is intended for educational and guidance purposes only.

It is not a medical device and should not replace professional medical
advice, diagnosis, or treatment.

In case of emergency, always contact local emergency services
immediately.

------------------------------------------------------------------------

# License

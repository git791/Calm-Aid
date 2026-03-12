from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from google import genai
from google.genai import types
import base64, os, json, asyncio
from PIL import Image
import io

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

SYSTEM_PROMPT = """You are CalmAid, an emergency first aid voice assistant.
Rules:
- Open with ONE short sentence of calm reassurance.
- Give numbered, step-by-step first aid instructions. Be concise.
- Never diagnose. Never prescribe medication.
- End EVERY response with: "If this is a serious emergency, please call 911 immediately."
- Keep total response under 130 words — it will be read aloud.
- If an image is provided, describe what you observe and tailor advice to it.
- If situation is unclear, give general safety advice and ask for more detail."""

class AidRequest(BaseModel):
    text: str = ""
    image_b64: str = ""

async def stream_gemini(parts):
    try:
        response = client.models.generate_content_stream(
            model="gemini-2.5-flash",
            contents=parts,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT,
                max_output_tokens=300,
            )
        )
        for chunk in response:
            if chunk.text:
                data = json.dumps({"chunk": chunk.text})
                yield f"data: {data}\n\n"
                await asyncio.sleep(0)
        yield f"data: {json.dumps({'done': True})}\n\n"
    except Exception as e:
        yield f"data: {json.dumps({'error': str(e)})}\n\n"

@app.post("/api/aid/stream")
async def stream_aid(req: AidRequest):
    if not req.text.strip() and not req.image_b64:
        raise HTTPException(status_code=400, detail="Provide text or image")

    parts = []
    if req.text.strip():
        parts.append(req.text.strip())
    if req.image_b64:
        img_bytes = base64.b64decode(req.image_b64)
        img = Image.open(io.BytesIO(img_bytes)).convert("RGB")
        # Convert PIL image to bytes for new SDK
        buf = io.BytesIO()
        img.save(buf, format="JPEG")
        img_part = types.Part.from_bytes(data=buf.getvalue(), mime_type="image/jpeg")
        parts.append(img_part)

    return StreamingResponse(
        stream_gemini(parts),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "X-Accel-Buffering": "no",
        }
    )

@app.get("/health")
def health():
    return {"status": "ok"}

app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")
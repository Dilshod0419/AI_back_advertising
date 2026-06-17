from fastapi import FastAPI, HTTPException, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from fastapi.staticfiles import StaticFiles

from database import engine
import models
from schemas import AdTextRequest, AdBannerRequest
import services

# ✅ Server ishga tushganda jadvallarni avtomat yaratadi
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI Ad Generator API",
    version="3.0",
    description="Sun'iy intellekt yordamida reklama matnlari va bannerlari yaratish"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "https://advertising-ai.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.mount("/upload", StaticFiles(directory="upload"), name="upload")

@app.get("/")
def read_root():
    return {
        "status": "✅ Backend ishlayapti",
        "version": "3.0",
        "endpoints": [
            "POST /api/v1/generate-text",
            "POST /api/v1/generate-banner"
        ]
    }


@app.post("/api/v1/generate-text")
async def generate_ad_text(request: AdTextRequest):
    """
    Matn reklamasi generatsiyasi (Streaming).
    Frontend dan chunklarni real vaqtda o'qishi mumkin.
    """
    try:
        return StreamingResponse(
            services.stream_ad_text(request),
            media_type="text/plain; charset=utf-8"   # ✅ charset qo'shildi (O'zbek harflari uchun)
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Matn yaratishda xatolik: {str(e)}")


@app.post("/api/v1/generate-banner")
async def generate_ad_banner(request: AdBannerRequest):
    """
    Banner (rasm) generatsiyasi.
    Javob: image/jpeg baytlari.
    """
    try:
        image_bytes = services.generate_ad_banner_bytes(request)
        return Response(
            content=image_bytes,
            media_type="image/jpeg",
            headers={
                # ✅ Brauzer rasmni cache qilmasligi uchun
                "Cache-Control": "no-cache",
                "Content-Length": str(len(image_bytes))
            }
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Banner yaratishda xatolik: {str(e)}")

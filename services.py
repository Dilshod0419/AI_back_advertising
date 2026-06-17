from google import genai
from google.genai import types as genai_types
from config import settings
import prompts
from database import SessionLocal
from models import GeneratedAd

# ✅ Client faqat bir marta yaratiladi
client = genai.Client(api_key=settings.GEMINI_API_KEY)

# for model in client.models.list():
#     print(model.name)

for model in client.models.list():
    if "image" in model.name.lower():
        print(model.name)

# ✅ Global print loop olib tashlandi (server har ishga tushganda chiqarardi)


def stream_ad_text(request):
    """Gemini-dan matnni stream qilib olib, bazaga saqlaydi"""

    categories_str = ", ".join(request.categories) if request.categories else "Ko'rsatilmagan"
    sale_price_str = f"{request.sale_price} $" if request.sale_price else "Chegirma yo'q"

    prompt = prompts.get_ad_text_prompt(
        product_name=request.product_name,
        brand_name=request.brand_name,
        categories_str=categories_str,
        price=request.price,
        sale_price=sale_price_str,
        description=request.description,
        product_url=request.product_url,
        ad_type=request.ad_type,
        ad_tone=request.ad_tone
    )

    full_text = ""

    try:
        response_stream = client.models.generate_content_stream(
            model="gemini-2.5-flash",
            contents=prompt
        )

        for chunk in response_stream:
            if chunk.text:
                full_text += chunk.text
                yield chunk.text

    except Exception as e:
        yield f"\n[Xatolik yuz berdi: {str(e)}]"
        return

    # ✅ Stream tugagach bazaga saqlaymiz
    if full_text:
        db = SessionLocal()
        try:
            new_ad = GeneratedAd(
                product_name=request.product_name,
                brand_name=request.brand_name,
                category=categories_str,
                price=request.price,
                sale_price=request.sale_price,
                description=request.description,
                generated_text=full_text
            )
            db.add(new_ad)
            db.commit()
            db.refresh(new_ad)
        except Exception as e:
            db.rollback()
            print(f"DB saqlashda xatolik: {e}")
        finally:
            db.close()


def generate_ad_banner_bytes(request) -> bytes:
    """Gemini Imagen orqali rasm baytlarini yaratadi"""

    image_prompt = prompts.get_ad_banner_prompt(
        product_name=request.product_name,
        brand_name=request.brand_name,
        description=request.description
    )

    # Imagen modellarini navbat bilan sinab ko'ramiz
    # (API kalitingizga qarab qaysi biri ishlashini tekshiramiz)
    models_to_try = [
        "imagen-4.0-generate-001",
        # "imagen-3.0-generate-002",
    ]

    last_error = None

    for model_name in models_to_try:
        try:
            print(f"🖼️ {model_name} sinab ko'rilmoqda...")
            result = client.models.generate_images(
                model=model_name,
                prompt=image_prompt,
                config={
                    "number_of_images": 1,
                    "output_mime_type": "image/jpeg",
                    "aspect_ratio": request.aspect_ratio or "1:1",
                }
            )
            image_bytes = result.generated_images[0].image.image_bytes
            print(f"✅ Banner yaratildi: {len(image_bytes)} bytes ({model_name})")
            return image_bytes

        except Exception as e:
            print(f"⚠️ {model_name} ishlamadi: {e}")
            last_error = e
            continue

    # Hech qaysi model ishlamasa aniq xato qaytaramiz
    raise Exception(
        f"Imagen modeli ishlamadi. "
        f"API kalitingiz Imagen ga ruxsat bermagan bo'lishi mumkin. "
        f"So'nggi xato: {last_error}"
    )






# from google import genai

# Bu yerga AIza... bilan boshlanadigan haqiqiy API keyni qo'ying


# client = genai.Client(api_key=API_KEY)

# try:
#     print("Model sinovdan o'tmoqda...")

#     result = client.models.generate_images(
#         model="imagen-4.0-fast-generate-001",
#         prompt="Modern smartphone advertising banner, professional marketing design"
#     )

#     print("MUVAFFAQIYAT!")
#     print(result)

# except Exception as e:
#     print("XATOLIK:")
#     print(repr(e))

    
# from google import genai
# from config import settings

# print("KEY =", settings.GEMINI_API_KEY[:10])

# client = genai.Client(
#     api_key=settings.GEMINI_API_KEY
# )

# try:
#     for model in client.models.list():
#         print(model.name)

# except Exception as e:
#     print("XATOLIK:", repr(e))


# from google import genai
# from config import settings

# client = genai.Client(api_key=settings.GEMINI_API_KEY)

# try:
#     response = client.models.generate_content(
#         model="gemini-2.5-flash-image",
#         contents="Create a professional smartphone advertising banner"
#     )

#     print(response)

# except Exception as e:
#     print("XATO:")
#     print(repr(e))
# def get_ad_text_prompt(
#     product_name: str,
#     brand_name: str,
#     categories_str: str,
#     price,
#     sale_price: str,
#     description: str,
#     product_url: str,
#     ad_type: str,
#     ad_tone: str
# ) -> str:
#     """O'zbekcha sotuvchi reklama matni uchun prompt"""

#     # ✅ Narx ko'rsatilmagan bo'lsa chiroyli ko'rsatamiz
#     price_str = f"{price} $" if price else "Ko'rsatilmagan"

#     return f"""
# Siz professional o'zbek kopiraytersiz. Quyidagi mahsulot ma'lumotlaridan foydalanib, jozibali va sotuvchi reklama matni yozing.
# Matn FAQAT O'ZBEK tilida bo'lsin.

# # MAHSULOT MA'LUMOTLARI:
# - Mahsulot nomi: {product_name}
# - Brend: {brand_name}
# - Kategoriya: {categories_str}
# - Eski narxi: {price_str}
# - Yangi (Chegirma) narxi: {sale_price}
# - Tavsif: {description}
# - Mahsulot havolasi: {product_url if product_url else "Ko'rsatilmagan"}

# # REKLAMA FORMATI:
# - Platforma: {ad_type}
# - Ohang: {ad_tone}

# # QAT'IY QOIDALAR:
# 1. Agar 'Ad Type' = Email bo'lsa, xatga 'Mavzu:' (Subject line) ham qo'shing.
# 2. Agar 'sale_price' bor bo'lsa, chegirma va foydani (FOMO) kuchli ta'kidlang.
# 3. Agar mahsulot havolasi berilgan bo'lsa, matn yakunida uni chiroyli joylashtiring.
# 4. Ortiqcha texnik izohlarsiz, faqat tayyor reklama matnini va mos emojilarni qaytaring.
# 5. Markdown formatidan foydalanmang (**, ## kabi belgilar ishlatmang).
# """


# def get_ad_banner_prompt(product_name: str, brand_name: str, description: str) -> str:
#     """Imagen uchun inglizcha rasm prompti"""
#     return (
#         f"Professional studio commercial product photography of {product_name} by {brand_name}. "
#         f"Context: {description}. High resolution, clean white background, "
#         f"premium commercial lighting, photorealistic, 8k quality."
#     )


def get_ad_text_prompt(
    product_name: str,
    brand_name: str,
    categories_str: str,
    price,
    sale_price: str,
    description: str,
    product_url: str,
    ad_type: str,
    ad_tone: str
) -> str:
    """Ko'p tilli sotuvchi reklama matni uchun prompt"""

    # ✅ Narx ko'rsatilmagan bo'lsa chiroyli ko'rsatamiz
    price_str = f"{price} $" if price else "Ko'rsatilmagan"

    return f"""
Siz professional ko'p tilli kopiraytersiz. Quyidagi mahsulot ma'lumotlaridan foydalanib, jozibali va sotuvchi reklama matni yozing.

# TIL QOIDASI:
Quyidagi "Tavsif" maydonidagi matn qaysi tilda yozilgan bo'lsa (masalan, o'zbek, rus, ingliz, yoki boshqa til), reklama matnini ANIQ SHU TILDA yozing. Tilni avtomatik aniqlang va unga mos ravishda javob bering. Agar tavsif bir necha tilning aralashmasi bo'lsa, eng ko'p ishlatilgan tilni tanlang.

# MAHSULOT MA'LUMOTLARI:
- Mahsulot nomi: {product_name}
- Brend: {brand_name}
- Kategoriya: {categories_str}
- Eski narxi: {price_str}
- Yangi (Chegirma) narxi: {sale_price}
- Tavsif: {description}
- Mahsulot havolasi: {product_url if product_url else "Ko'rsatilmagan"}

# REKLAMA FORMATI:
- Platforma: {ad_type}
- Ohang: {ad_tone}

# QAT'IY QOIDALAR:
1. Agar 'Ad Type' = Email bo'lsa, xatga 'Mavzu:' (Subject line) ham qo'shing — bu ham aniqlangan tilda bo'lsin.
2. Agar 'sale_price' bor bo'lsa, chegirma va foydani (FOMO) kuchli ta'kidlang.
3. Agar mahsulot havolasi berilgan bo'lsa, matn yakunida uni chiroyli joylashtiring.
4. Ortiqcha texnik izohlarsiz, faqat tayyor reklama matnini va mos emojilarni qaytaring.
5. Markdown formatidan foydalanmang (**, ## kabi belgilar ishlatmang).
6. Reklama matnidagi barcha matn (sarlavha, tavsif, CTA va boshqalar) bir xil, aniqlangan tilda bo'lsin — tillarni aralashtirmang.
"""


def get_ad_banner_prompt(product_name: str, brand_name: str, description: str) -> str:
    """Imagen uchun inglizcha rasm prompti"""
    return (
        f"Professional studio commercial product photography of {product_name} by {brand_name}. "
        f"Context: {description}. High resolution, clean white background, "
        f"premium commercial lighting, photorealistic, 8k quality."
    )
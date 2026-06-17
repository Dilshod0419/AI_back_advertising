from pydantic import BaseModel, field_validator
from typing import Optional, List

# 📝 Matn reklamasi uchun model
class AdTextRequest(BaseModel):
    product_name: str
    brand_name: str
    categories: Optional[List[str]] = []
    price: Optional[float] = None       # ✅ Optional qilindi (None bo'lishi mumkin)
    sale_price: Optional[float] = None
    description: str
    product_url: Optional[str] = ""     # ✅ image_url olib tashlandi — backend ishlatmaydi
    ad_type: str
    ad_tone: str

    # ✅ Bo'sh string kelsa None ga aylantiradi
    @field_validator("price", "sale_price", mode="before")
    @classmethod
    def empty_string_to_none(cls, v):
        if v == "" or v is None:
            return None
        return v

# 🖼️ Reklama banneri uchun model
class AdBannerRequest(BaseModel):
    product_name: str
    brand_name: str
    description: str
    aspect_ratio: Optional[str] = "1:1"

from sqlalchemy import Column, Integer, String, Float, DateTime, Text
from database import Base
import datetime

class GeneratedAd(Base):
    __tablename__ = "generated_ads"

    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String(255), index=True)
    brand_name = Column(String(255))
    category = Column(String(255), nullable=True)
    price = Column(Float, nullable=True)
    sale_price = Column(Float, nullable=True)
    description = Column(Text)
    generated_text = Column(Text, nullable=True)
    banner_path = Column(String(500), nullable=True)

    # ✅ utcnow deprecated edi, timezone-aware ga o'zgartirildi
    created_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.datetime.now(datetime.timezone.utc)
    )

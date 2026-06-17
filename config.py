import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")
    DATABASE_URL: str = os.getenv("DATABASE_URL", "")

    def validate(self):
        if not self.GEMINI_API_KEY:
            raise ValueError("GEMINI_API_KEY .env faylida topilmadi!")
        if not self.DATABASE_URL:
            raise ValueError("DATABASE_URL .env faylida topilmadi!")

settings = Settings()

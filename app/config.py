import os
from dotenv import load_dotenv

# .env faylini yuklash
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
AI_API_KEY = os.getenv("AI_API_KEY")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN topilmadi! Iltimos, .env faylini tekshiring.")

import asyncio
import os
from aiohttp import web
from aiogram import Bot, Dispatcher
from app.config import BOT_TOKEN
from bot.handlers import router
from utils.logger import logger

# Render uchun oddiy veb-server (Bot xatolik berib o'chib qolmasligi uchun)
async def handle_ping(request):
    return web.Response(text="Bot ishlayapti!")

async def start_web_server():
    app = web.Application()
    app.router.add_get('/', handle_ping)
    runner = web.AppRunner(app)
    await runner.setup()
    # Render o'zi beradigan portni oladi, yo'qsa 8080 ni ishlatadi
    port = int(os.environ.get("PORT", 8080))
    site = web.TCPSite(runner, '0.0.0.0', port)
    await site.start()
    logger.info(f"Veb-server {port}-portda ishga tushdi.")

async def main():
    logger.info("Stomatologik AI bot ishga tushmoqda...")
    
    # Veb-serverni ishga tushirish
    await start_web_server()

    # Bot va Dispatcher obyektlarini yaratish
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    
    # Routerni ulash
    dp.include_router(router)
    
    # Eski xabarlarni o'tkazib yuborib, botni ishga tushirish
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Bot to'xtatildi.")

import asyncio
from aiogram import Bot, Dispatcher
from app.config import BOT_TOKEN
from bot.handlers import router
from utils.logger import logger

async def main():
    logger.info("Stomatologik AI bot ishga tushmoqda...")
    
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

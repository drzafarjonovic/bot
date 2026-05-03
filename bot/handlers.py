from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart

from bot.keyboards import get_main_keyboard

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        "Assalomu alaykum! Stomatologik AI yordamchisiga xush kelibsiz.",
        reply_markup=get_main_keyboard()
    )

@router.message(F.text == "Boshlash")
async def process_start_btn(message: Message):
    await message.answer("Tashxis jarayoni tez orada ishga tushadi. (Hozircha ishlab chiqilmoqda)")

@router.message(F.text == "Yordam")
async def process_help_btn(message: Message):
    await message.answer("Sizga qanday yordam bera olaman? Bu bot orqali stomatologik maslahatlar olishingiz mumkin bo'ladi.")

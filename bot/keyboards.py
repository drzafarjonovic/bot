from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_main_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Boshlash"),
                KeyboardButton(text="Yordam")
            ]
        ],
        resize_keyboard=True,
        input_field_placeholder="Quyidagi tugmalardan birini tanlang..."
    )
    return keyboard

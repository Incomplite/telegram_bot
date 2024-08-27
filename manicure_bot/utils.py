from aiogram import types

from manicure_bot.config import settings

kb = [
    [
        types.KeyboardButton(text="Записаться"),
        types.KeyboardButton(text="Мои записи"),
        types.KeyboardButton(text="Доступные команды")
    ]
]
keyboard = types.ReplyKeyboardMarkup(
    keyboard=kb,
    resize_keyboard=True,
    input_field_placeholder="Выберите, что вам подходит",
    one_time_keyboard=True
)

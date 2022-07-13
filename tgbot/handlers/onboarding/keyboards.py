from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup

from tgbot.handlers.onboarding.manage_data import SECRET_LEVEL_BUTTON
from tgbot.handlers.onboarding.static_text import github_button_text, secret_level_button_text
from tgbot.handlers.onboarding.static_text import (
    passenger_title, driver_title, contact_center, permanent_driver, control_panel
)



def make_keyboard_for_start_command() -> ReplyKeyboardMarkup:
    buttons = [
        [passenger_title, driver_title],
        [contact_center, permanent_driver],
        [control_panel],
    ]

    return ReplyKeyboardMarkup(buttons, resize_keyboard=True)

def make_keyboard_for_passenger() -> ReplyKeyboardMarkup:
    buttons = [
        # Viloyatlar bo'lishi kerak
        ["⬅️ Ortga"]
    ]

    return ReplyKeyboardMarkup(buttons, resize_keyboard=True)

def make_keyboard_for_driver() -> ReplyKeyboardMarkup:
    buttons = [
        ["🪧E'lon yaratish"],
        ["⬅️ Ortga"]
    ]

    return ReplyKeyboardMarkup(buttons, resize_keyboard=True)

def make_keyboard_for_create_advertisement() -> ReplyKeyboardMarkup:
    buttons = [
        # Viloyatlar bo'lishi kerak
        ["❌ Bekor qilish"]
    ]

    return ReplyKeyboardMarkup(buttons, resize_keyboard=True)


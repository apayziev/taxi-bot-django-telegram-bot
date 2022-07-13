import datetime

from django.utils import timezone
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update
from telegram.ext import CallbackContext, ConversationHandler

from tgbot.handlers.onboarding import static_text
from tgbot.handlers.utils.info import extract_user_data_from_update
from tgbot.models import User
from tgbot.handlers.onboarding.keyboards import make_keyboard_for_start_command
from tgbot.handlers.onboarding import keyboards

PASSENGER, DRIVER, ADVERTISEMENT, ADVERTISEMENT_CANCEL = range(4)


def command_start(update: Update, context: CallbackContext) -> None:
    u, created = User.get_user_and_created(update, context)

    if created:
        text = static_text.start_created.format(first_name=u.first_name)
    else:
        text = static_text.start_not_created.format(first_name=u.first_name)

    update.message.reply_text(text=text,
                              reply_markup=make_keyboard_for_start_command())

def secret_level(update: Update, context: CallbackContext) -> None:

    # callback_data: SECRET_LEVEL_BUTTON variable from manage_data.py
    """ Pressed 'secret_level_button_text' after /start command"""
    user_id = extract_user_data_from_update(update)['user_id']
    text = static_text.unlock_secret_room.format(
        user_count=User.objects.count(),
        active_24=User.objects.filter(updated_at__gte=timezone.now() - datetime.timedelta(hours=24)).count()
    )

    context.bot.edit_message_text(
        text=text,
        chat_id=user_id,
        message_id=update.callback_query.message.message_id,
        parse_mode=ParseMode.HTML
    )

def contact_us_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
    f"<b><i>{static_text.contact_us_button_text}</i></b>",
    reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton(text='📞 Administrator', url='https://t.me/UzMenedger')],
    ]),
    parse_mode=ParseMode.HTML
)

def permanent_driver_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
    f"<b>{static_text.how_to_be_permanent_driver_text}</b>",
    reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton(text='📞 Administrator', url='https://t.me/UzMenedger')],
    ]),
    parse_mode=ParseMode.HTML
)
   

def passenger_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(text=static_text.ask_passenger_location_text,
                              reply_markup=keyboards.make_keyboard_for_passenger())
    return PASSENGER

def driver_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(text=static_text.create_advertise_text,
                              reply_markup=keyboards.make_keyboard_for_driver())
    return DRIVER

def create_advertisement_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(text=static_text.ask_driver_location_text,
                              reply_markup=keyboards.make_keyboard_for_create_advertisement())
    
    return ADVERTISEMENT

def cancel_advertisement_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(text="E'lon bekor qilindi! ✅",
                              reply_markup=keyboards.make_keyboard_for_start_command())
   
    return ConversationHandler.END




def back_to_main_page(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(text="Orqaga qaytdingiz.",
                              reply_markup=keyboards.make_keyboard_for_start_command())
    return ConversationHandler.END
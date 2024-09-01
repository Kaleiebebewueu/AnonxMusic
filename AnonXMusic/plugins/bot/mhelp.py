from typing import Union

from pyrogram import filters, types
from pyrogram.types import InlineKeyboardMarkup, Message

from AnonXMusic import app
from AnonXMusic.utils import help_pannel
from AnonXMusic.utils.database import get_lang
from AnonXMusic.utils.decorators.language import LanguageStart, languageCB
from AnonXMusic.utils.inline.mhelp import mhelp_back_markup, mprivate_help_panel
from config import BANNED_USERS, START_IMG_URL, SUPPORT_CHAT
from strings import get_string, mhelpers


@app.on_message(filters.command(["mhelp"]) & filters.private & ~BANNED_USERS)
@app.on_callback_query(filters.regex("msettings_back_helper") & ~BANNED_USERS)
async def helper_private(
    client: app, update: Union[types.Message, types.CallbackQuery]
):
    is_callback = isinstance(update, types.CallbackQuery)
    if is_callback:
        try:
            await update.answer()
        except:
            pass
        chat_id = update.message.chat.id
        language = await get_lang(chat_id)
        _ = get_string(language)
        keyboard = mhelp_pannel(_, True)
        await update.edit_message_text(
            _["help_1"].format(SUPPORT_CHAT), reply_markup=keyboard
        )
    else:
        try:
            await update.delete()
        except:
            pass
        language = await get_lang(update.chat.id)
        _ = get_string(language)
        keyboard = mhelp_pannel(_)
        await update.reply_photo(
            photo=START_IMG_URL,
            caption=_["help_1"].format(SUPPORT_CHAT),
            reply_markup=keyboard,
        )

@app.on_callback_query(filters.regex("mhelp_callback") & ~BANNED_USERS)
@languageCB
async def helper_cb(client, CallbackQuery, _):
    callback_data = CallbackQuery.data.strip()
    cb = callback_data.split(None, 1)[1]
    keyboard = mhelp_back_markup(_)
    if cb == "mhb1":
        await CallbackQuery.edit_message_text(helpers.MHELP_1, reply_markup=keyboard)
    elif cb == "mhb2":
        await CallbackQuery.edit_message_text(helpers.MHELP_2, reply_markup=keyboard)
    elif cb == "mhb3":
        await CallbackQuery.edit_message_text(helpers.MHELP_3, reply_markup=keyboard)
    elif cb == "mhb4":
        await CallbackQuery.edit_message_text(helpers.MHELP_4, reply_markup=keyboard)
    elif cb == "mhb5":
        await CallbackQuery.edit_message_text(helpers.MHELP_5, reply_markup=keyboard)
    elif cb == "mhb6":
        await CallbackQuery.edit_message_text(helpers.MHELP_6, reply_markup=keyboard)
    elif cb == "mhb7":
        await CallbackQuery.edit_message_text(helpers.MHELP_7, reply_markup=keyboard)
    elif cb == "mhb8":
        await CallbackQuery.edit_message_text(helpers.MHELP_8, reply_markup=keyboard)
    elif cb == "mhb9":
        await CallbackQuery.edit_message_text(helpers.MHELP_9, reply_markup=keyboard)
    elif cb == "mhb10":
        await CallbackQuery.edit_message_text(helpers.MHELP_10, reply_markup=keyboard)
    elif cb == "mhb11":
        await CallbackQuery.edit_message_text(helpers.MHELP_11, reply_markup=keyboard)
    elif cb == "mhb12":
        await CallbackQuery.edit_message_text(helpers.MHELP_12, reply_markup=keyboard)
    elif cb == "mhb13":
        await CallbackQuery.edit_message_text(helpers.MHELP_13, reply_markup=keyboard)
    elif cb == "mhb14":
        await CallbackQuery.edit_message_text(helpers.MHELP_14, reply_markup=keyboard)
    elif cb == "mhb15":
        await CallbackQuery.edit_message_text(helpers.MHELP_15, reply_markup=keyboard)

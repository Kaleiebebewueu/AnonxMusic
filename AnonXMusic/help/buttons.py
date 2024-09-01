from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters, enums 

class BUTTONS(object):
    MBUTTON = [
              [
                  InlineKeyboardButton("+", callback_data="music HELP_HELP1"),
                  InlineKeyboardButton("+", callback_data="music HELP_HELP2"),
                  InlineKeyboardButton("+", callback_data="music HELP_HELP3")
               ],
               [
                  InlineKeyboardButton("⌯ ʙᴀᴄᴋ ⌯", callback_data=f"settingsback_helper",)
               ]
    ]

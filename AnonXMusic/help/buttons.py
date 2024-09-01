from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters, enums 

class BUTTONS(object):
    MBUTTON = [
              [
                  InlineKeyboardButton("+", callback_data="mplus HELP_HELP1"),
                  InlineKeyboardButton("+", callback_data="mplus HELP_HELP2"),
                  InlineKeyboardButton("+", callback_data="mplus HELP_HELP3")
               ],
               [
                  InlineKeyboardButton("⩤", callback_data=f"settings_back_helper"), 
                  InlineKeyboardButton("⩥", callback_data=f"managebot123 settings_back_helper"),
               ]]

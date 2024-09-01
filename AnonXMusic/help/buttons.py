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
                  InlineKeyboardButton("⩤", callback_data=f"settings_back_helper"), 
                  InlineKeyboardButton("⩥", callback_data=f"sanatani settings_back_helper"),
               ]]

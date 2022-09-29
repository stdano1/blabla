from faulthandler import disable
import os
from bot import bot as stdlogo
from config import Config
from bot.plugins import*
from pyrogram import filters, idle, Client
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto, CallbackQuery
from requests import get
import pytz
import asyncio
import logging
from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
import requests
from bot.utils import (HELPTEXT, HELPBTNS, LOGOTEXT, STARTBTNS, STARTTEXT, GROUPBTN, ABOUTTEXT, ABOUTBTNS,
                    LOGOTEXT, LOGOBTNS, BOTTEXT, BOTBTNS)
from bot import LOGGER
from bot.helpers.humanbytes import humanbytes
from bot.helpers.database.add_user import AddUserToDatabase, AddChatToDatabase

BOTUNAME="thelogogenbot"



@stdlogo.on_message(filters.private & filters.incoming & filters.command(["start"]))
async def startmsgpm(_, message):
    await AddUserToDatabase(_, message)
    await message.reply_text(
    text = STARTTEXT.format(message.from_user.mention),
    reply_markup = STARTBTNS,
    disable_web_page_preview=True
  )


@stdlogo.on_message(filters.private & filters.incoming & filters.command(["help"]))
async def helpmsgpm(_, message):
  await message.reply_text(
    text=HELPTEXT,
    reply_markup=HELPBTNS,
    disable_web_page_preview=True
  )

@stdlogo.on_message(filters.command(["start","help"]) & ~filters.private)
async def startmsg(_, message):
    await AddChatToDatabase(_, message)
    await message.reply_text(
    text=f"Hello👋\nStart Me In PM For More Details",
    reply_markup=GROUPBTN
  )

#===========================Callbacks===========================
@stdlogo.on_callback_query(filters.regex("startmenu"))
async def logomenu(_, query: CallbackQuery):
    await query.edit_message_text(STARTTEXT.format(query.from_user.mention),
        reply_markup=STARTBTNS,
     disable_web_page_preview=True
    )

@stdlogo.on_callback_query(filters.regex("helpmenu"))
async def logomenu(_, query: CallbackQuery):
    await query.edit_message_text(HELPTEXT,
        reply_markup=HELPBTNS,
     disable_web_page_preview=True
    )

@stdlogo.on_callback_query(filters.regex("aboutmenu"))
async def logomenu(_, query: CallbackQuery):
    await query.edit_message_text(ABOUTTEXT,
        reply_markup=ABOUTBTNS,
     disable_web_page_preview=True
    )

@stdlogo.on_callback_query(filters.regex("logomenu"))
async def logomenu(_, query: CallbackQuery):
    await query.edit_message_text(LOGOTEXT,
        reply_markup=LOGOBTNS,
     disable_web_page_preview=True
    )

@stdlogo.on_callback_query(filters.regex("botmenu"))
async def logomenu(_, query: CallbackQuery):
    await query.edit_message_text(BOTTEXT,
        reply_markup=BOTBTNS,
     disable_web_page_preview=True
    )

#===========================Callbacks-end===========================

    
    
async def main_startup():
    await stdlogo.start()
    logging.info("bot is alive")
    try:
        await stdlogo.send_message(chat_id=-1001487511637, text="**[Logo Gen Bot✨](https://t.me/ThelogoGenbot) is Online**.\n\n__Powered By [CGS OFFICIAL](https://t.me/CGSUpdates)⚡️__", disable_web_page_preview=True)
    except:
        logging.warn("error")
    await idle()

loop = asyncio.get_event_loop()
loop.run_until_complete(main_startup())

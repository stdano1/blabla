import os
import re
import shutil
import random
import requests
from bot import bot
from os import getenv
from io import BytesIO
from requests import get
from pyrogram import Client
from pyrogram import filters
from bot.plugins.fsub import ForceSub
from bot.utils import LOGOGEN, LOGOGENBTNS
from telegraph import upload_file
from bot.helpers.database.database import (
        add_logo,
        del_logo
)
from PIL import Image, ImageDraw, ImageFont
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

@bot.on_message(filters.command("logo") & ~filters.forwarded)
@ForceSub
async def logomake(_, message: Message):
    if len(message.command) != 2:
        return await message.reply_text("Please give a text.\nEx:`/logo cgs` ")
    else:
        pass
    m = await message.reply('Designing your logo...wait!') 
    text = message.text.split(None, 1)[1]
    img = Image.open("./bot/resources/maskbg.jpg")
    draw = ImageDraw.Draw(img)
    image_widthz, image_heightz = img.size
    pointsize = 500
    fillcolor = "gold"
    shadowcolor = "blue"
    font = ImageFont.truetype("./bot/resources/FLASHING.OTF", 400)
    w, h = draw.textsize(text, font=font)
    h += int(h*0.21)
    image_width, image_height = img.size
    draw.text(((image_widthz-w)/2, (image_heightz-h)/2), text, font=font, fill=(255, 255, 255))
    x = (image_widthz-w)/2
    y= ((image_heightz-h)/2+6)
    draw.text((x, y), text, font=font, fill="white", stroke_width=0, stroke_fill="yellow")
    maskstd = f'maskstd.png'
    img.save(maskstd, "png")
    await m.edit("📤Uploading...")
    await message.reply_photo(
                photo=maskstd,
                caption= LOGOGEN.format(message.from_user.mention if message.from_user else "Anonymous Admin"),
                reply_markup = LOGOGENBTNS
            )
    await m.delete()
    response = upload_file(maskstd)
    tg_url = f"{response[0]}"
    await add_logo(tg_url)
    
    if os.path.exists(maskstd):
            os.remove(maskstd)


@bot.on_message(filters.command("plogo") & ~filters.forwarded)
@ForceSub
async def logomake(_, message: Message):
    if len(message.command) != 2:
        return await message.reply_text("Please give a text.\nEx:`/plogo cgs` ")
    else:
        pass
    m = await message.reply('Designing your logo...wait!')
    text = message.text.split(None, 1)[1]
    img = Image.open("./bot/resources/20220404_091513.jpg")
    draw = ImageDraw.Draw(img)
    image_widthz, image_heightz = img.size
    pointsize = 500
    fillcolor = "gold"
    shadowcolor = "blue"
    font = ImageFont.truetype("./bot/resources/THE HUMBLE.OTF", 370)
    w, h = draw.textsize(text, font=font)
    h += int(h*0.21)
    image_width, image_height = img.size
    draw.text(((image_widthz-w)/2, (image_heightz-h)/2), text, font=font, fill=(255, 255, 255))
    x = (image_widthz-w)/2
    y= ((image_heightz-h)/2+6)
    draw.text((x, y), text, font=font, fill="white", stroke_width=4, stroke_fill="magenta")
    plogostd = f'plogostd.png'
    img.save(plogostd, "png")
    await m.edit("`📤Uploading. . .`")
    await message.reply_photo(
                photo=plogostd,
                caption= LOGOGEN.format(message.from_user.mention if message.from_user else "Anonymous Admin"),
                reply_markup = LOGOGENBTNS
            )
    await m.delete()
    response = upload_file(plogostd)
    tg_url = f"{response[0]}"
    await add_logo(tg_url)
    if os.path.exists(plogostd):
            os.remove(plogostd)

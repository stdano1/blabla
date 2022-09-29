import os
import random
from bot import bot
from pyrogram import Client
from pyrogram import filters, idle
from bot.utils import LOGOGEN, LOGOGENBTNS
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from telegraph import upload_file
from bot.helpers.database.database import (
        add_logo,
        del_logo
)


@bot.on_message(filters.command("saber") & ~filters.bot & ~filters.forwarded)
async def weather(_, message):
    if len(message.command) < 2:
            return await message.reply_text("**Provide Some Text To Create Logo**\nEx:`/saber CGS` ")
    m = await message.reply_text("`✍️ Creating. . .`")
    TXTSTD = message.text.split(None, 1)[1] if len(message.command) < 3 else message.text.split(None, 1)[1].replace(" ", "%20")
    # background
    folder = "./bot/resources/pantherbgs"
    imgpath = random.choice(os.listdir(folder))
    bgfile = folder+'/'+imgpath
    # open resources
    STDIMG = Image.open(bgfile)
    FONTSTD = ImageFont.truetype("./bot/resources/FLASHING.OTF", 160)
    x = STDIMG.width//2
    y = STDIMG.height//2
    EDITSTD = ImageDraw.Draw(STDIMG)
    EDITSTD.text((x, 1000), TXTSTD, font=FONTSTD, anchor="mm", fill='black')
    saberestd = f'saberbystd.png'
    STDIMG.save(saberestd, "png")
    await m.edit('`📤 Uploading. . .`')
    await message.reply_photo(photo = saberestd,
                              caption = LOGOGEN.format(message.from_user.mention if message.from_user else "Anonymous Admin"),
                              reply_markup = LOGOGENBTNS)
    response = upload_file(saberestd)
    tg_url = f"{response[0]}"
    await add_logo(tg_url)
    await m.delete()
    if os.path.exists(saberestd):
            os.remove(saberestd)

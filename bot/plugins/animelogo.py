import os
import random
from bot import bot
from pyrogram import filters, idle
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from bot.plugins.fsub import ForceSub
from bot.utils import LOGOGEN, LOGOGENBTNS
from telegraph import upload_file
from bot.helpers.database.database import (
        add_logo,
        del_logo
)


@bot.on_message(filters.command("anime") & ~filters.bot & ~filters.forwarded)
@ForceSub
async def weather(_, message):
    if len(message.command) < 2:
            return await message.reply_text("**Provide Some Text To Create Logo**\nEx:`/anime cgs` ")
    m = await message.reply_text("`✍️Creating. . .`")
    TXTSTD = message.text.split(None, 1)[1] if len(message.command) < 3 else message.text.split(None, 1)[1].replace(" ", "%20")
    # background
    folder = "./bot/resources/bgs"
    imgpath = random.choice(os.listdir(folder))
    bgfile = folder+'/'+imgpath
    # anime
    folder2 = "./bot/resources/animes"
    imgpath2 = random.choice(os.listdir(folder2))
    anmfile = folder2+'/'+imgpath2
    # open resources
    STDIMG = Image.open(bgfile)
    ANMIMG = Image.open(anmfile)
    FONTSTD = ImageFont.truetype("./bot/resources/ROAD_RAGE.OTF", 170)
    x = STDIMG.width//2
    y = STDIMG.height//2
    # logo prosses
    STDIMG.paste(ANMIMG, ANMIMG)
    SHADOW = Image.new('RGBA', STDIMG.size)
    draw = ImageDraw.Draw(SHADOW)
    draw.text((640, 870), text=TXTSTD, fill='black', font=FONTSTD, anchor='mm', stroke_width=15, stroke_fill='black')
    SHADOW = SHADOW.filter(ImageFilter.BoxBlur(5))
    STDIMG.paste(SHADOW, SHADOW)
    EDITSTD = ImageDraw.Draw(STDIMG)
    EDITSTD.text((640, 870), TXTSTD, font=FONTSTD, anchor="mm", stroke_width=3, stroke_fill='black', fill='White')
    animestd = f'animebystd.png'
    STDIMG.save(animestd, "png")
    await m.edit('`📤Uploading. . .`')
    await message.reply_photo(photo = animestd,
                              caption= LOGOGEN.format(message.from_user.mention if message.from_user else "Anonymous Admin"),
                              reply_markup = LOGOGENBTNS
                             )
    await m.delete()
    response = upload_file(animestd)
    tg_url = f"{response[0]}"
    await add_logo(tg_url)
    if os.path.exists(animestd):
            os.remove(animestd)

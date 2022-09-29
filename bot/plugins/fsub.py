from functools import wraps
from bot import bot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant

FTEXT = f" **🚫Access Denied🚫** \nYou Must Join [Our Channel](https://t.me/CGSUpdates)To Use Me. So, Please Join it & Try Again. "
CAPTION_BTN = InlineKeyboardMarkup(
            [[InlineKeyboardButton("🙋Join Channel", url="https://t.me/CGSUpdates")]])

def ForceSub(func):
    @wraps(func)
    async def bot_message(_, message):
        try:
            await message._client.get_chat_member(-1001179611522, message.from_user.id)
        except UserNotParticipant:
            return await message.reply_text(
                        text=FTEXT,
                        reply_markup=CAPTION_BTN,
                        disable_web_page_preview=True) 
        return await func(_, message)    
    return bot_message

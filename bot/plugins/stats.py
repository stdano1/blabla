import os
import time
import shutil
import psutil
import pyrogram
import subprocess
from pyrogram import filters
from sys import version as pyver
from bot.helpers.humanbytes import humanbytes
from bot import bot as app
from pyrogram.types import Message
from pyrogram import filters, idle
from config import Config
from bot.helpers.database.database import (
    is_served_user,
    get_served_users,
    add_served_user,
    remove_served_user,
    is_served_chat,
    get_served_chats,
    add_served_chat,
    remove_served_chat,
    add_banned_user,
    del_banned_user,
    count_banned_users,
    count_logos
)

@app.on_message(filters.command("stats") & filters.user(Config.OWNER))
async def stats(_, message: Message):
    name = message.from_user.id
    m = await message.reply_text(text=f"Getting Stats...")
    total, used, free = shutil.disk_usage(".")
    total = humanbytes(total)
    used = humanbytes(used)
    free = humanbytes(free)
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    served_chats = len(await get_served_chats())
    served_chats = []
    chats = await get_served_chats()
    for chat in chats:
        served_chats.append(int(chat["chat_id"]))
    served_users = len(await get_served_users())
    served_users = []
    banned_users = await count_banned_users()
    logos = await count_logos()
    users = await get_served_users()
    for user in users:
        served_users.append(int(user["bot_users"]))

    await m.edit(
        text=f"""
📊 Bot Stats 📊

**👥 Users**
• ⚡️ Total Users: `{len(served_users)}`
• ⚡️ Total Groups : `{len(served_chats)}`
• 💥 Total Baned Users: `{banned_users}`
• 🚧 Total users & groups : {int((len(served_chats) + len(served_users)))}
• 🔰Total created logos : `{logos}`

**🎛 Systerm usage**
• 💽 Total Disk Space: {total}
• 💿 Used Space: {used}({disk_usage}%)
• 📊 Free Space: {free}
• 🔋 CPU Usage: {cpu_usage}%
• 🖲 Ram Usage: {ram_usage}% 

Status requested by [{message.from_user.first_name}](tg://user?id={message.from_user.id})""")
    
@app.on_message(filters.command("ban") & filters.user(Config.OWNER))
async def ban_user(_, message: Message):
    ban_msg = await message.reply("`Processing… ⏳`")
    try:
        user_id = message.text.split(None, 1)[1]
    except:
        return await ban_msg.edit("Give an user id to ban 😈")
    await add_banned_user(user_id)
    await ban_msg.edit(f"**Successfully banned that user ✅** \n\n**User ID :** `{user_id}`")

@app.on_message(filters.command("unban") & filters.user(Config.OWNER))
async def unban_user(_, message: Message):
    unban_msg = await message.reply("`Processing… ⏳`")
    try:
        user_id = message.text.split(None, 1)[1]
    except:
        return await unban_msg.edit("Give an user id to unban 😇")
    await del_banned_user(user_id)
    await unban_msg.edit(f"**Successfully unbanned that user ✅** \n\n**User ID :** `{user_id}`")

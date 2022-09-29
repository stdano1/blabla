#=================================================================================================
# Copyright (C) 2022 by szsupunma@Github, < https://github.com/szsupunma >.
# Released under the "GNU v3.0 License Agreement".
# All rights reserved.
#=================================================================================================
import datetime
import motor.motor_asyncio
from config import Config
import os
from motor.motor_asyncio import AsyncIOMotorClient

DATABASE = Config.MONGODB_URI

mongo_client = AsyncIOMotorClient(DATABASE)
logo_db = mongo_client["std_logo"]
# Users Database
userdb = logo_db["userdb"]

#===================== User database ================================

async def is_served_user(user_id: int) -> bool:
    user = await userdb.find_one({"bot_users": user_id})
    if not user:
        return False
    return True

async def get_served_users() -> list:
    users = userdb.find({"bot_users": {"$gt": 0}})
    if not users:
        return []
    users_list = []
    for user in await users.to_list(length=1000000000):
        users_list.append(user)
    return users_list

async def add_served_user(user_id: int):
    is_served = await is_served_user(user_id)
    if is_served:
        return
    return await userdb.insert_one({"bot_users": user_id})

async def remove_served_user(user_id: int):
    is_served = await is_served_user(user_id)
    if is_served:
        return
    return await userdb.delete_one({"bot_users": user_id})

#===================== groups  database ================================

async def get_served_chats() -> list:
    chats = userdb.find({"chat_id": {"$lt": 0}})
    if not chats:
        return []
    chats_list = []
    async for chat in userdb.find({"chat_id": {"$lt": 0}}):
        chats_list.append(chat)
    return chats_list

async def is_served_chat(chat_id: int) -> bool:
    chat = await userdb.find_one({"chat_id": chat_id})
    if not chat:
        return False
    return True

async def add_served_chat(chat_id: int):
    is_served = await is_served_chat(chat_id)
    if is_served:
        return
    return await userdb.insert_one({"chat_id": chat_id})

async def remove_served_chat(chat_id: int):
    is_served = await is_served_chat(chat_id)
    if not is_served:
        return
    return await userdb.delete_one({"chat_id": chat_id})

#===================== ban  database ================================
# Banned users database
b_user_db = logo_db["banuserdb"]

async def add_banned_user(user_id):
    new_user_id = int(user_id)
    is_exist = await b_user_db.find_one({"banned_user_id": new_user_id})
    if is_exist:
        return
    await b_user_db.insert_one({"banned_user_id": new_user_id})

async def del_banned_user(user_id):
    del_user_id = int(user_id)
    is_exist = await b_user_db.find_one({"banned_user_id": del_user_id})
    if is_exist:
        await b_user_db.delete_one({"banned_user_id": del_user_id})
    else:
        return

async def is_user_in_bdb(user_id):
    u_id = int(user_id)
    is_exist = await b_user_db.find_one({"banned_user_id": u_id})
    if is_exist:
        return True
    return False

async def count_banned_users():
    users = await b_user_db.count_documents({})
    return users

async def get_banned_users_list():
    return [banned_users_list async for banned_users_list in b_user_db.find({})]

#===================== logo count  database ================================
# Copyright (C) 2022 by sithijatd@Github, < https://github.com/sithijatd >.
# Logo counter database
Logo_c_db = logo_db["logocounterdb"]

async def add_logo(tg_url):
    new_logo_url = tg_url
    is_exist = await Logo_c_db.find_one({"logo_url": new_logo_url})
    if is_exist:
        return
    await Logo_c_db.insert_one({"logo_url": new_logo_url})

async def del_logo(tg_url):
    del_logo_url = tg_url
    is_exist = await Logo_c_db.find_one({"logo_url": del_logo_url})
    if is_exist:
        await Logo_c_db.delete_one({"logo_url": del_logo_url})
    else:
        return

async def is_logo_in_db(tg_url):
    l_url = tg_url
    is_exist = await Logo_c_db.find_one({"logo_url": l_url})
    if is_exist:
        return True
    return False

async def count_logos():
    logos = await Logo_c_db.count_documents({})
    return logos

async def get_logo_list():
    return [logo_url_list async for logo_url_list in Logo_c_db.find({})]

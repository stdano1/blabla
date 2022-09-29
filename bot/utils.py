

import os
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ForceReply

BOTNAME="Logo Gen Bot"
BOTUNAME="ThelogoGenbot"

STARTTEXT = """👋Hello {}

I am CGS Logo Gen bot
I can create simple logos for you.

[TEAM CGS](https://t.me/cgsupdates) All Right Received©
"""

STARTBTNS = InlineKeyboardMarkup(
            [       
                [
                    InlineKeyboardButton("Help", callback_data="helpmenu"),
                    InlineKeyboardButton("About", callback_data="aboutmenu")
                ], 
                [ 
                    InlineKeyboardButton("Channel", url="https://t.me/CGSUpdates")           
                ],
                [ 
                    InlineKeyboardButton("Add To Group", url="http://t.me/ThelogoGenbot?startgroup=true")           
                ]
            ]
        )

GROUPBTN = InlineKeyboardMarkup(
           [
             [
               InlineKeyboardButton("Visit PM", url="https://t.me/sithijatdbot")
             ],
           ]
       ) 

HELPTEXT = """ Hello !

I have some commands.
Try bellow buttons to 
know about them👇. """

HELPBTNS = InlineKeyboardMarkup(
           [
             [
               InlineKeyboardButton("☘️Logo☘️", callback_data="logomenu"),
               InlineKeyboardButton("🍁Bot🍁", callback_data="botmenu")
             ],
             [
               InlineKeyboardButton("🔙Back", callback_data="startmenu")
             ],
           ]
       ) 

ABOUTTEXT = """⚡This logo bot is mainly powered with pyrogram & pillow.

Credits 💳
This bot is made with the help of many peoples,
So credit of this bot should be go to them 

⚡Powered By [CGS OFFICIAL](https://t.me/CGSUpdates)⚡️"""

ABOUTBTNS = InlineKeyboardMarkup(
           [
             [
               InlineKeyboardButton("🔙Back", callback_data="startmenu")
             ]
           ]
       ) 

LOGOTEXT = """෴Logo Commands෴

This is my logo making commands🔥
Try them and Get a fun.

•/logo {text} - simple logo.
•/plogo {text} - pink logo.
•/anime {text} - random anime logo.
•/saber {text} - saber tooth tiger logo.

More logos update in soon. """

LOGOBTNS = InlineKeyboardMarkup(
           [[
               InlineKeyboardButton("🔙Back", callback_data="helpmenu")
           ]]
         )

BOTTEXT = """ ෴Bot commands෴

•/start - Start bot.
•/help - Get Help.

 """

BOTBTNS = InlineKeyboardMarkup(
           [[
               InlineKeyboardButton("🔙Back", callback_data="helpmenu")
           ]]
         )

LOGOGEN = """
🔰**Logo Created**🔰
**✅Successfully**
〢───────────────〣

👤**Requestor**: {}
🔥**Created by**: [Logo Gen Bot✨](https://t.me/ThelogoGenbot)

〣───────────────〢
[©️ CGS OFFICIAL](https://t.me/CGSUpdates)
"""

LOGOGENBTNS = InlineKeyboardMarkup(
      [
        [
         InlineKeyboardButton(text="⚜️ Updates ⚜️", url=f"https://t.me/CGSUpdates") 
        ],
        [
        InlineKeyboardButton(text="🚸 Support 🚸", url=f"https://t.me/CGSsupport") 
        ]
      ]      
  )




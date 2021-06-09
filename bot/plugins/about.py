from pyrogram import Filters, InlineKeyboardMarkup, InlineKeyboardButton

from ..screenshotbot import ScreenShotBot


ABOUT_TEXT = """
<b>A screeshot generator bot with your custom watermark, also support sample vedio generating system

Name : Screenshot Bot

Language : python

Framework : pyrogram

Server : heroku

Developer : @Maxxcoderz

And if you want to add any other Modes, request it in @CoderzSupport</b>
"""



@ScreenShotBot.on_message(Filters.private & Filters.command("about"))
async def help(c, m):
    
    await m.reply_text(
        text=ABOUT_TEXT.format(m.from_user.first_name),
        quote=True
    )

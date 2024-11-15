from pyrogram import *
from pyrogram.types import *
from Tanjiro import TanjiroUb, SUDO
import asyncio
import time

@TanjiroUb.on_message(filters.command("promote", prefixes=".") & filters.user(SUDO))
async def promoting(_, message):
     global new_admin
     if message.from_user.id == TanjiroUb.me.id:
         mes = message
     else:
         mes = await message.reply_text("....")
     if not message.reply_to_message:
         return await mes.edit("use this command reply")
     reply = message.reply_to_message
     chat_id = message.chat.id
     new_admin = reply.from_user
     admin = message.from_user     
     bot_stats = await TanjiroUb.get_chat_member(chat_id, "self")
     if not bot_stats.privileges:
         return await mes.edit("opps! iam not admin")     
     elif not bot_stats.privileges.can_promote_members:
         return await mes.edit("i dont have admin rights ")   
     await mes.edit("Promoting")
     await TanjiroUb.promote_chat_member(
        message.chat.id,
        new_admin.id,
        privileges=pyrogram.types.ChatPrivileges(
        can_change_info=True,
        can_delete_messages=True,
        can_pin_messages=True,
        can_invite_users=True,
        can_manage_video_chats=True,
        can_restrict_members=True
     ))
     await mes.edit(f"Alright!! Successful promoted")


@TanjiroUb.on_message(filters.command("demote", prefixes=".") & filters.user(SUDO))
async def demote(_, message):
     global new_admin
     if message.from_user.id == TanjiroUb.me.id:
         mes = message
     else:
         mes = await message.reply_text("....")
     if not message.reply_to_message:
         return await mes.edit("use this command reply")
     reply = message.reply_to_message
     chat_id = message.chat.id
     new_admin = reply.from_user
     admin = message.from_user     
     bot_stats = await TanjiroUb.get_chat_member(chat_id, "self")
     if not bot_stats.privileges:
         return await mes.edit("hey dude iam not admin")     
     elif not bot_stats.privileges.can_promote_members:
         return await mes.edit("i dont have admin rights ")
     await mes.edit("`Proccing...`")
     await TanjiroUb.promote_chat_member(
        chat_id,
        new_admin.id,
        privileges=pyrogram.types.ChatPrivileges(
        can_change_info=False,
        can_invite_users=False,
        can_delete_messages=False,
        can_restrict_members=False,
        can_pin_messages=False,
        can_promote_members=False,
        can_manage_chat=False,
        can_manage_video_chats=False    
     ))
     await mes.edit(f"Hmm!! demoted 🥺")

from pyrogram import *
from pyrogram.types import *
from Tanjiro import TanjiroUb


@TanjiroUb.on_message(filters.command("promote", prefixes=".") & filters.user(SUDO))
async def promoting(_, message):
     global new_admin
     if not message.reply_to_message:
         return await message.edit("use this command reply")
     reply = message.reply_to_message
     chat_id = message.chat.id
     new_admin = reply.from_user
     admin = message.from_user     
     bot_stats = await piro.get_chat_member(chat_id, "self")
     if not bot_stats.privileges:
         return await message.edit("opps! iam not admin")     
     elif not bot_stats.privileges.can_promote_members:
         return await message.edit("i dont have admin rights ")   
     msg = await message.edit("Promoting")
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
     await message.edit(f"Alright!! Successful promoted")


@Tanjiro.on_message(filters.command("demote", prefixes=".") & filters.user(SUDO))
async def demote(_, message):
     global new_admin
     if not message.reply_to_message:
         return await message.edit("use this command reply")
     reply = message.reply_to_message
     chat_id = message.chat.id
     new_admin = reply.from_user
     admin = message.from_user     
     bot_stats = await piro.get_chat_member(chat_id, "self")
     if not bot_stats.privileges:
         return await message.edit("hey dude iam not admin")     
     elif not bot_stats.privileges.can_promote_members:
         return await message.edit("i dont have admin rights ")
     await message.edit("`Proccing...`")
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
     await message.edit(f"Hmm!! demoted 🥺")

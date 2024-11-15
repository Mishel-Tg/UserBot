from pyrogram import *
from pyrogram.types import *
from Tanjiro import TanjiroUb
import asyncio
import time

@TanjiroUb.on_message(filters.command("promote", prefixes=".") & filters.user(SUDO))
async def promoting(_, message):
     global new_admin
     if not message.reply_to_message:
         return await message.edit("use this command reply")
     reply = message.reply_to_message
     chat_id = message.chat.id
     new_admin = reply.from_user
     admin = message.from_user     
     bot_stats = await TanjiroUb.get_chat_member(chat_id, "self")
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


@TanjiroUb.on_message(filters.command("demote", prefixes=".") & filters.user(SUDO))
async def demote(_, message):
     global new_admin
     if not message.reply_to_message:
         return await message.edit("use this command reply")
     reply = message.reply_to_message
     chat_id = message.chat.id
     new_admin = reply.from_user
     admin = message.from_user     
     bot_stats = await TanjiroUb.get_chat_member(chat_id, "self")
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

@TanjiroUb.on_message(filters.command("scrap", prefixes=".") & filters.me)
async def scarpmember(_, message):
    if len(message.command) < 2:
        return await message.reply("Please enter group user name or chat id to scrap.")
    
    chat_identifier = message.text.split(None, 1)[1]
    
    try:        
        chat_info = await TanjiroUb.get_chat(chat_identifier)
    except Exception as e:
        return await message.reply("Invalid group chat ID or username provided.")
    
    try:
        me = await TanjiroUb.get_chat_member(chat_info.id, message.from_user.id)        
        if me.status in [enums.ChatMemberStatus.MEMBER, enums.ChatMemberStatus.ADMINISTRATOR, enums.ChatMemberStatus.OWNER]:
            await message.reply("You are in the group. Proceeding to add members...")
            await performadd(chat_info.id, message)
        else:
            await message.reply("You are not in the group.")
    
    except Exception as e:
        return await message.reply("You are not in that group or do not have access to it.")

async def performadd(chat_id, message):
    time_start = time.time()
    success = 0
    fck = await message.reply("huhu 😗 Adding members...")
    
    async for member in TanjiroUb.get_chat_members(chat_id):
        try:
            if not member.user.is_bot:
                output = await TanjiroUb.add_chat_members(message.chat.id, member.user.id)
                if output:
                    success += 1
                await asyncio.sleep(2)
        except Exception as e:
            if not str(e) == "Telegram says: [400 CHAT_ADMIN_REQUIRED] - The method requires chat admin privileges (caused by 'messages.UpdatePinnedMessage')" and not str(e).startswith("Telegram says: [420 FLOOD_WAIT_X] - A wait"):
                print(e)
    
    await fck.delete()
    await message.reply(f"Successfully added {success} members\nTime taken: {int(time.time() - time_start)} seconds.")

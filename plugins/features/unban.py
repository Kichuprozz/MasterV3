from pyrogram import Client, filters
from plugins.functions.admin_check import admin_check
from plugins.functions.extract import extract_time, extract_user                               


@Client.on_message(filters.command(["unban", "unmute"]))
async def un_ban_user(_, message):
    is_admin = await admin_check(message)
    if not is_admin:
        return
    user_id, user_first_name = extract_user(message)
    try:
        await message.chat.unban_member(user_id=user_id)
    except Exception as error:
        await message.reply_text(str(error))
    else:
        if str(user_id).lower().startswith("@"):
            await message.reply_text(
                "ᴏᴋᴇʏ, ᴄʜᴀɴɢᴇᴅ... ɴᴏᴡ "
                f"{user_first_name} To "
                " ʏᴏᴜ ᴄᴀɴ'ᴛ ᴊᴏɪɴ ᴛʜᴇ ɢʀᴏᴜᴩ!"
            )
        else:
            await message.reply_text(
                "ᴏᴋᴇʏ, ᴄʜᴀɴɢᴇᴅ... ɴᴏᴡ "
                f"<a href='tg://user?id={user_id}'>"
                f"{user_first_name}"
                "</a> To "
                " ʏᴏᴜ ᴄᴀɴ'ᴛ ᴊᴏɪɴ ᴛʜᴇ ɢʀᴏᴜᴩ!"
            )

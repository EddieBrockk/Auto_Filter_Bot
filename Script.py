class script(object):
    START_TXT = """<b><u> কী গো! </u></b>

<b>ʜᴇʏ {}, {}</b>

<b>🤖 ɪ ᴀᴍ <a href=https://t.me/{}>{}</a>, ᴛʜᴇ ᴍᴏꜱᴛ ᴘᴏᴡᴇʀꜰᴜʟ ᴀᴜᴛᴏ ꜰɪʟᴛᴇʀ ʙᴏᴛ.</b>
"""

    GSTART_TXT = """<b> কী গো! </b>

<b>ʜᴇʏ {},</b>

<b>🤖 ɪ ᴀᴍ <a href=https://t.me/{}>{}</a>, ᴛʜᴇ ᴍᴏꜱᴛ ᴘᴏᴡᴇʀꜰᴜʟ ᴀᴜᴛᴏ ꜰɪʟᴛᴇʀ ʙᴏᴛ.</b>
"""

    HELP_TXT = """<b>
✨ ʜᴏᴡ ᴛᴏ ʀᴇǫᴜᴇꜱᴛ ᴅʀᴀᴍᴀꜱ & ᴍᴏᴠɪᴇꜱ ✨  

1️⃣ ꜱᴇᴀʀᴄʜ ᴛʜᴇ ᴄᴏʀʀᴇᴄᴛ ɴᴀᴍᴇ ᴏɴ ɢᴏᴏɢʟᴇ.  
2️⃣ ꜱᴇɴᴅ ᴛʜᴇ ɴᴀᴍᴇ ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ.  
3️⃣ ᴜꜱᴇ ᴛʜɪꜱ ꜰᴏʀᴍᴀᴛ:  

📌 ꜰᴏʀ ꜱᴇʀɪᴇꜱ:  
➤ ᴅʀᴀᴍᴀ ɴᴀᴍᴇ + S01  

📌 ꜰᴏʀ ʜɪɴᴅɪ ᴅʀᴀᴍᴀꜱ:  
➤ ᴅʀᴀᴍᴀ ɴᴀᴍᴇ + ʜɪɴᴅɪ  

📌 ꜰᴏʀ ᴍᴏᴠɪᴇꜱ:  
➤ ᴍᴏᴠɪᴇ ɴᴀᴍᴇ + ʏᴇᴀʀ (ᴇx: ᴊᴏᴋᴇʀ 2019)  
</b>"""

    ABOUT_TXT = """<b>╭────[ ᴍʏ ᴅᴇᴛᴀɪʟs ]────⍟
├⍟ Mʏ Nᴀᴍᴇ : <a href=https://t.me/{}>{}</a>
├⍟ Dᴇᴠᴇʟᴏᴘᴇʀ : <a href={}>ᴏᴡɴᴇʀ</a> 
├⍟ Lɪʙʀᴀʀʏ : Pyrogram
├⍟ Lᴀɴɢᴜᴀɢᴇ : Python 3
├⍟ Dᴀᴛᴀʙᴀsᴇ : MongoDB
├⍟ Bᴏᴛ Sᴇʀᴠᴇʀ : Heroku
├⍟ Bᴜɪʟᴅ Sᴛᴀᴛᴜs : ᴠ1.4 [ ꜱᴛᴀʙʟᴇ ]
╰───────────────⍟</b>"""

    RESTART_TXT = """
<b>{} Bᴏᴛ Rᴇsᴛᴀʀᴛᴇᴅ !

📅 Dᴀᴛᴇ : <code>{}</code>
⏰ Tɪᴍᴇ : <code>{}</code>
🌐 Tɪᴍᴇᴢᴏɴᴇ : Asia/Kolkata
🛠️ Bᴜɪʟᴅ Sᴛᴀᴛᴜs: v1.4 [Sᴛᴀʙʟᴇ]
</b>"""

    CHANNELS = """
<b>⚡ ɢʀᴏᴜᴘs & ᴄʜᴀɴɴᴇʟs ɪɴғᴏ ⚡ 

▫ ꜰᴀsᴛᴇsᴛ ʙᴏᴛs  
▫ ꜰʀᴇᴇ & ᴇᴀsʏ ᴛᴏ ᴜsᴇ  
▫ 𝟸𝟺x𝟽 sᴇʀᴠɪᴄᴇꜱ  
</b>"""

    MULTI_STATUS_TXT = """<b>╭────[ 🗃 ᴅᴀᴛᴀʙᴀsᴇ 1 ]────⍟</b>
├⋟ ᴀʟʟ ᴜsᴇʀs ⋟ <code>{}</code>
├⋟ ᴀʟʟ ɢʀᴏᴜᴘs ⋟ <code>{}</code>
├⋟ ᴀʟʟ ꜰɪʟᴇs ⋟ <code>{}</code>
├⋟ ᴜsᴇᴅ sᴛᴏʀᴀɢᴇ ⋟ <code>{}</code>
├⋟ ꜰʀᴇᴇ sᴛᴏʀᴀɢᴇ ⋟ <code>{}</code>

<b>├────[ 🗳 ᴅᴀᴛᴀʙᴀsᴇ 2 ]────⍟</b>   
├⋟ ᴀʟʟ ꜰɪʟᴇs ⋟ <code>{}</code>
├⋟ ꜱɪᴢᴇ ⋟ <code>{}</code>
├⋟ ꜰʀᴇᴇ ⋟ <code>{}</code>

<b>├────[ 🤖 ʙᴏᴛ ᴅᴇᴛᴀɪʟs ]────⍟</b>   
├⋟ ᴜᴘᴛɪᴍᴇ ⋟ {}
├⋟ ʀᴀᴍ ⋟ <code>{}%</code>
├⋟ ᴄᴘᴜ ⋟ <code>{}%</code>

<b>╰─────────────────────⍟</b>
"""

    STATUS_TXT = """<b>╭────[ 🗃 ᴅᴀᴛᴀʙᴀsᴇ ]────⍟</b>
├⋟ ᴀʟʟ ᴜsᴇʀs ⋟ <code>{}</code>
├⋟ ᴀʟʟ ɢʀᴏᴜᴘs ⋟ <code>{}</code>
├⋟ ᴀʟʟ ꜰɪʟᴇs ⋟ <code>{}</code>
├⋟ ᴜsᴇᴅ sᴛᴏʀᴀɢᴇ ⋟ <code>{}</code>
├⋟ ꜰʀᴇᴇ sᴛᴏʀᴀɢᴇ ⋟ <code>{}</code>

<b>├────[ 🤖 ʙᴏᴛ ᴅᴇᴛᴀɪʟs ]────⍟</b>   
├⋟ ᴜᴘᴛɪᴍᴇ ⋟ {}
├⋟ ʀᴀᴍ ⋟ <code>{}%</code>
├⋟ ᴄᴘᴜ ⋟ <code>{}%</code>
<b>╰─────────────────────⍟</b>
"""

    PRE_STREAM = ""
    PRE_STREAM_ALERT = ""

    CUDNT_FND = SPELLING_ERROR_TXT = """<b>‼️ ꜱᴘᴇʟʟɪɴɢ ᴍɪꜱᴛᴀᴋᴇ!</b>  
<b>ᴄʜᴏᴏꜱᴇ ᴛʜᴇ ᴄᴏʀʀᴇᴄᴛ ᴍᴏᴠɪᴇ ʙᴇʟᴏᴡ 👇</b>"""

    DEL_MSG = """⚠️ ᴛʜɪꜱ ꜰɪʟᴇ ᴡɪʟʟ ʙᴇ ᴅᴇʟᴇᴛᴇᴅ ɪɴ <b><u><code>{}</code></u></b>"""

    I_CUDNT = """<b>sᴏʀʀʏ, ɴᴏ ꜰɪʟᴇꜱ ꜰᴏᴜɴᴅ ꜰᴏʀ {} 😕  
ᴄʜᴇᴄᴋ ʏᴏᴜʀ sᴘᴇʟʟɪɴɢ ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ.</b>"""

    I_CUD_NT = """<b>ɪ ᴄᴏᴜʟᴅɴ'ᴛ ꜰɪɴᴅ ᴀɴʏ ᴍᴏᴠɪᴇ ʀᴇʟᴀᴛᴇᴅ ᴛᴏ {}.  
ᴘʟᴇᴀꜱᴇ ᴀᴅᴅ ʏᴇᴀʀ ᴏʀ ᴄʜᴇᴄᴋ ɢᴏᴏɢʟᴇ ꜱᴘᴇʟʟɪɴɢ.</b>"""

    MVE_NT_FND = NOT_FOUND_TXT = """<b>😌 ᴍᴏᴠɪᴇ ɴᴏᴛ ꜰᴏᴜɴᴅ ɪɴ ᴅᴀᴛᴀʙᴀsᴇ.</b>"""

    TOP_ALRT_MSG = """ꜱᴇᴀʀᴄʜɪɴɢ ɪɴ ᴍʏ ᴅᴀᴛᴀʙᴀsᴇ..."""

    MELCOW_ENG = """<b>👋 ʜᴇʏ {},\n\n🌟 ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ {}\n\n🔍 ᴛʏᴘᴇ ᴍᴏᴠɪᴇ/ꜱᴇʀɪᴇꜱ ɴᴀᴍᴇ ᴛᴏ ꜱᴇᴀʀᴄʜ.</b>"""

    DISCLAIMER_TXT = """<b>ᴛʜɪꜱ ᴘʀᴏᴊᴇᴄᴛ ɪꜱ ᴏᴘᴇɴ ꜱᴏᴜʀᴄᴇ ᴀɴᴅ ᴅᴍᴄᴀ ᴄᴏᴍᴘʟɪᴀɴᴛ.  
ᴄᴏɴᴛᴇɴᴛ ɪꜱ ɪɴᴅᴇxᴇᴅ ꜰʀᴏᴍ ᴛᴇʟᴇɢʀᴀᴍ.</b>"""

    DONATION = """<b>👋 ʜᴇʏ {},  
If you want to support development, you may donate voluntarily.  
(ᴏᴘᴛɪᴏɴᴀʟ)</b>"""

    SINFO = """
Series Request Format:

Example: Loki S01E01
"""

    CAPTION = """<b><a href="https://t.me/sonchar_backup">{file_name}</a></b>\n<b>⚜️ Powered By : <a href="https://t.me/wolfmasterxd">[ wolf ]</a></b>"""

    MOVIE_UPDATE_NOTIFY_TXT = """
<b>📥 New {tag} Added</b>

<b>✨ Title :</b> <code>{filename}</code>
<b>🎭 Genres :</b> {genres}
<b>🎧 Audio :</b> {language}
"""

    IMDB_TEMPLATE_TXT = """<b><a href={url}>{title} ({year})</a>

⭐ Rating : {rating}
🎭 Genre : {genres}
🎧 Audio : {languages}

Requested by: {message.from_user.mention}</b>
"""

    LOGO = r"""BOT WORKING PROPERLY"""

    PAGE_TXT = ""
    PURCHASE_TXT = ""
    PREMIUM_TEXT = ""
    PREMIUM_STAR_TEXT = ""
    PREMIUM_UPI_TEXT = ""
    PREMIUM_END_TEXT = ""
    BPREMIUM_TXT = ""
    PREPLANS_TXT = ""
    FREE_TXT = ""
    UPI_TXT = ""
    QR_TXT = ""

    SOURCE_TXT = """<b>OPEN SOURCE PROJECT  
Do not sell this code.</b>"""

    SETTING_TXT = """Group Settings Commands:
• /settings  
• /set_shortner  
• /set_shortner_2  
• /set_shortner_3  
• /set_tutorial  
• /set_tutorial_2  
• /set_tutorial_3  
• /set_time  
• /set_time_2  
• /set_log_channel  
• /set_fsub  
• /remove_fsub  
• /reset_group  
• /details
"""

    VERIFICATION_TEXT = """<b>👋 ʜᴇʏ {},  
Please verify to continue using unlimited access.</b>"""

    VERIFY_COMPLETE_TEXT = """<b>Verification Completed ✓</b>"""

    SECOND_VERIFICATION_TEXT = VERIFICATION_TEXT
    SECOND_VERIFY_COMPLETE_TEXT = VERIFY_COMPLETE_TEXT

    THIRDT_VERIFICATION_TEXT = VERIFICATION_TEXT
    THIRDT_VERIFY_COMPLETE_TEXT = VERIFY_COMPLETE_TEXT

    VERIFIED_LOG_TEXT = """User Verified ✓  
Name: {}  
ID: {}  
Date: {}  
Step: {}"""

    ADMIN_CMD = """Admin Commands:

• /start  
• /stats  
• /del_msg  
• /movie_update  
• /pm_search  
• /verify  
• /logs  
• /delete  
• /users  
• /chats  
• /leave  
• /disable  
• /ban  
• /unban  
• /broadcast  
• /grp_broadcast  
• /deletefiles  
• /send  
• /restart  
"""

    GROUP_CMD = """Group Commands:

• /settings  
• /set_shortner  
• /set_shortner_2  
• /set_shortner_3  
• /set_tutorial  
• /set_tutorial_2  
• /set_tutorial_3  
• /set_time  
• /set_time_2  
• /set_log_channel  
• /set_fsub  
• /remove_fsub  
• /reset_group  
• /details  
"""

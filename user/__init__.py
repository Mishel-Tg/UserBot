from pyrogram import Client

API_ID = int(os.environ.get('API_ID'))  

SUDO = [1867106198]  
tanjiro = Client(
        "Userbot",
        session_string=SESSION,
        api_id=API_ID,
        api_hash=API_HASH,
        plugins=dict(root="user/Bot") )

    

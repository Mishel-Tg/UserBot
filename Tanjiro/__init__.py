from pyrogram import Client

API_ID = int(os.environ.get('API_ID'))  
API_HASH = os.environ.get('API_HASH')  
SESSION = os.environ.get('SESSION')  

SUDO = [1867106198]  

Tanjiro = Client(
        "ub",
        session_string=SESSION,
        api_id=API_ID,
        api_hash=API_HASH,
        plugins=dict(root="Tanjiro/user") )

    

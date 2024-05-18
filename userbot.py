from pyrogram import *
import re
import os
from os import environ
import asyncio
import json

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.strip().lower() in ["on", "true", "yes", "1", "enable", "y"]: return True
    elif value.strip().lower() in ["off", "false", "no", "0", "disable", "n"]: return False
    else: return default

API_ID = int(os.environ.get('API_ID', ''))
API_HASH = os.environ.get('API_HASH', '')
SESSION = os.environ.get('SESSION', '')


piro = Client("Gojo", session_string=SESSION, api_id=API_ID, api_hash=API_HASH, plugins=dict(root="user"))


print("Your session started")

piro.run()

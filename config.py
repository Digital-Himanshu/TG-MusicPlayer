import os
from dotenv import load_dotenv
from pyrogram import Client
from pytgcalls import PyTgCalls

# For Local Deploy
if os.path.exists(".env"):
    load_dotenv(".env")

API_ID = int(os.getenv("API_ID", "6"))
API_HASH = os.getenv("API_HASH", "eb06d4abfb49dc3eeb1aeb98ae0f581e")
SESSION = os.getenv("SESSION")
HNDLR = os.getenv("HNDLR", "!")


bot = Client(SESSION, API_ID, API_HASH, plugins=dict(root="VCBot"))
call_py = PyTgCalls(bot)

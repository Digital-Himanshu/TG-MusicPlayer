import os
import asyncio
from pyrogram import Client, idle
from pytgcalls import PyTgCalls
from pytgcalls import idle as pyidle
from config import bot, player, call_py

async def vcclient():
   await bot.start()
   print("UserBot Started")
   await call_py.start()
   print("Vc Client Started")
   await pyidle()
   await idle()

asyncio.get_event_loop().run_until_complete(vcclient())

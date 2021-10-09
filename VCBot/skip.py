from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Message
from config import bot, call_py, HNDLR, contact_filter
from VCBot.handlers import skip_current_song
from VCBot.queues import QUEUE, clear_queue

@Client.on_message(contact_filter & filters.command(['skip'], prefixes=f"{HNDLR}"))
async def skip(client, m: Message):
   chat_id = m.chat.id
   op = await skip_current_song(chat_id)
   if op==0:
      await m.reply("`Nothing Is Playing`")
   elif op==1:
      await m.reply("`Queue is Empty, Leaving Voice Chat...`")
   else:
      await m.reply(f"**Skipped ⏭** \n**🎧 Now Playing** - [{op[0]}]({op[1]})", disable_web_page_preview=True)

@Client.on_message(contact_filter & filters.command(['end', 'stop'], prefixes=f"{HNDLR}"))
async def stop(client, m: Message):
   chat_id = m.chat.id
   if chat_id in QUEUE:
      try:
         await call_py.leave_group_call(chat_id)
         clear_queue(chat_id)
         await m.reply("**Stopped Streaming ⏹️**")
      except Exception as e:
         await m.reply(f"**ERROR** \n`{e}`")
   else:
      await m.reply("`Nothing is Streaming`")
   
@Client.on_message(contact_filter & filters.command(['pause'], prefixes=f"{HNDLR}"))
async def pause(client, m: Message):
   chat_id = m.chat.id
   if chat_id in QUEUE:
      try:
         await call_py.pause_stream(chat_id)
         await m.reply("**Paused Streaming ⏸️**")
      except Exception as e:
         await m.reply(f"**ERROR** \n`{e}`")
   else:
      await m.reply("`Nothing is Streaming`")
      
@Client.on_message(contact_filter & filters.command(['resume'], prefixes=f"{HNDLR}"))
async def resume(client, m: Message):
   chat_id = m.chat.id
   if chat_id in QUEUE:
      try:
         await call_py.resume_stream(chat_id)
         await m.reply("**Resumed Streaming ▶**")
      except Exception as e:
         await m.reply(f"**ERROR** \n`{e}`")
   else:
      await m.reply("`Nothing is Streaming`")

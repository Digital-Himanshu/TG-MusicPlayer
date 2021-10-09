from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Message
from VCBot.queues import QUEUE, get_queue
from config import HNDLR, contact_filter

@Client.on_message(filters.command(['playlist', 'queue'], prefixes=f"{HNDLR}"))
async def playlist(client, m: Message):
   chat_id = m.chat.id
   if chat_id in QUEUE:
      chat_queue = get_queue(chat_id)
      if len(chat_queue)==1:
         await m.reply(f"**🎧 NOW PLAYING:** \n[{chat_queue[0][0]}]({chat_queue[0][2]})", disable_web_page_preview=True)
      else:
         QUE = f"**🎧 NOW PLAYING:** \n[{chat_queue[0][0]}]({chat_queue[0][2]}) \n\n**⏯ PLAYLIST:**"
         l = len(chat_queue)
         for x in range (1, l):
            hmm = chat_queue[x][0]
            hmmm = chat_queue[x][2]
            QUE = QUE + "\n" + f"**#{x}** - [{hmm}]({hmmm})"
         await m.reply(QUE, disable_web_page_preview=True)
   else:
      await m.reply("`Nothing is Streaming`")

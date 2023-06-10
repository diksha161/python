from telethon import events
from .. import bot
import asyncio
import openai

openai.api_key = "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"
#openai.api_key = openai_key

@bot.on(events.NewMessage(incoming=True,pattern= "(?i)/ask"))
async def _gpt(event):
  # if event.sender_id ==()
  await event.reply("yes! you are my Developer, you developed me very well")
  # else:
   # await evemt .reply("you are user:nice to meet you")
  await event.reply(event)
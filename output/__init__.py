from telethon import TelegramClient
import logging
import time 


openai_key = "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"
api_id = "1125689"

api_hash = "4772d1792ed194020a8fb06a91ffb8fa"

bot_token = "6124528141:AAG3-US44QNwqjRZ1ZZzH9pMunqu6cdZiws"

bot = TelegramClient("input", api_id, api_hash
   ).start(bot_token = bot_token)
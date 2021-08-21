
import os
from pyrogram import Client

# TG_BOT_TOKEN = os.environ["TG_BOT_TOKEN"]
# APP_ID = int(os.environ["APP_ID"])
# API_HASH = os.environ["API_HASH"]
#ADMIN = int(os.environ.get("ADMIN"))
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN")
APP_ID = int(os.environ.get("APP_ID"))
API_HASH = os.environ.get("API_HASH")

start_message = """Hey! I’m Nerd - your budgeting assistant. I’ll help setup budget, weekly targets and keep you on track. Select a goal to begin 🔥

Type option number👇
1. New Gadget, vacation etc
2. Investing money
3. Building emergency fund
4. Paying off debt
5. Just saving"""

plugins = dict(root="plugins")
print("starting...")
bot = Client(
    "nerdbot",
    bot_token=TG_BOT_TOKEN,
    api_id=APP_ID,
    api_hash=API_HASH,
    plugins=plugins
)
print("running...")
bot.run()


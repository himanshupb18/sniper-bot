
# sniper_bot.py
import os
from dotenv import load_dotenv
from telegram_alert import send_telegram_message

load_dotenv()

API_KEY = os.getenv("API_KEY")
CLIENT_ID = os.getenv("CLIENT_ID")
PASSWORD = os.getenv("PASSWORD")
PAN = os.getenv("PAN")

# Sample use: send a Telegram message
send_telegram_message("✅ Sniper Bot Started Successfully.")

# Future: place order logic goes here

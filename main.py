import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

load_dotenv()

TOKEN = os.getenv('TELEGRAM_TOKEN')

async def start(update, context):
    await update.message.reply_text('Hello, World!')
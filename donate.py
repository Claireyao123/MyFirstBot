from telegram.ext import Dispatcher,CommandHandler,CallbackQueryHandler
import random
from telegram import InlineKeyboardMarkup, InlineKeyboardButton

def donate(update,context):
    update.message.reply_text("""
    Thanks for visiting our robot :) please click this website in order to donate some money for our website and robots!
    https://5fad4508177dc.site123.me/
    """)

def add_handler(dp:Dispatcher):
    donations_handler = CommandHandler('donations', donate)
    dp.add_handler(donations_handler)
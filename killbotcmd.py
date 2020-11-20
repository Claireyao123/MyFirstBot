from telegram.ext import Dispatcher,CommandHandler
import random

def killbot(update, context):
    update.message.reply_text("一番搏斗后，大家看到 Salted Fish 拿着一把带血的刀扬长而去。。。\n R.I.P")

def add_handler(dp:Dispatcher):
    killbot_handler = CommandHandler('killbot', killbot)
    dp.add_handler(killbot_handler)
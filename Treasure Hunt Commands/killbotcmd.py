from telegram.ext import Dispatcher,CommandHandler
import random

def killbot(update, context):
    update.message.reply_text("不！要！杀！我！！！我对你们那么好，真是好心没好报啊！")

def add_handler(dp:Dispatcher):
    killbot_handler = CommandHandler('killbot', killbot)
    dp.add_handler(killbot_handler)
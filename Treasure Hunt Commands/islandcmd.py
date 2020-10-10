from telegram.ext import Dispatcher,CommandHandler
import random

def island(update, context):
    update.message.reply_text("你和你的船员们一起在岛上的树林里露宿去了，结果被岛上的野人发现并杀死了！\n历经千辛万苦走到这一步已经很厉害了！这 5500XP 是你的奖励！")

def add_handler(dp:Dispatcher):
    island_handler = CommandHandler('island', island)
    dp.add_handler(island_handler)
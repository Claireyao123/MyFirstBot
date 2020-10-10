from telegram.ext import Dispatcher,CommandHandler
import random
result18 = ["还好还好，逃过一劫！", "啊呀！一不小心就丢掉了 40XP !", "天呐天呐！你最近是怎么回事啦！居然丢掉了 90XP !", "一路走好！等等！200XP 拿来！"]

def startpunish(update, context):
    update.message.reply_text(random.choice(result18))

def add_handler(dp:Dispatcher):
    startpunish_handler = CommandHandler('startpunish', startpunish)
    dp.add_handler(startpunish_handler)
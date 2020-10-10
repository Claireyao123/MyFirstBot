from telegram.ext import Dispatcher,CommandHandler
import random

def nowalk(update, context):
    update.message.reply_text("你和你的船员们因为没有出门而没看见巨乌贼海怪克拉肯在啃你们的船，当你反应过来已经迟了...人生啊，太残酷了，也只能怪你自己太不小心了...")

def add_handler(dp:Dispatcher):
    nowalk_handler = CommandHandler('nowalk', nowalk)
    dp.add_handler(nowalk_handler)
from telegram.ext import Dispatcher,CommandHandler
import random

def late(update, context):
    update.message.reply_text("风平浪静的早上大家都在睡懒觉，海盗船以极快的速度向你们移来，咚的一声，你的船被大炮击中了！船舱进了好多水。你虽然拼命的挣扎，但还是被残酷的生活淘汰了，你低估了这次航行的危险，接着你的大脑一片空白...")

def add_handler(dp:Dispatcher):
    late_handler = CommandHandler('late', late)
    dp.add_handler(late_handler)
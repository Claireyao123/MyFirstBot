from telegram.ext import Dispatcher,CommandHandler
import random

def dance(update, context):
    update.message.reply_text("欢乐的舞曲，快乐的舞姿，所有人都非常开心！你似乎稳定了大家都心情！\n第二天早上是早起还是晚起呢？\n输入 /early 来早起\n输入 /late 来晚起")

def add_handler(dp:Dispatcher):
    dance_handler = CommandHandler('dance', dance)
    dp.add_handler(dance_handler)
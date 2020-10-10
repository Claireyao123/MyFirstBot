from telegram.ext import Dispatcher,CommandHandler
import random

def happy(update, context):
    update.message.reply_text("所有人尽情狂欢，大家越来越糊涂和开心，结果船被风吹到了百慕大三角，所有人葬身海低...")

def add_handler(dp:Dispatcher):
    happy_handler = CommandHandler('happy', happy)
    dp.add_handler(happy_handler)
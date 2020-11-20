from telegram.ext import Dispatcher,CommandHandler
import random

def rest(update, context):
    update.message.reply_text("船员们累坏了，迫不及待的会船舱休息去了。第二天早上是早起还是晚起呢？\n输入 /early 来早起\n输入 /late 来晚起")

def add_handler(dp:Dispatcher):
    rest_handler = CommandHandler('rest', rest)
    dp.add_handler(rest_handler)
from telegram.ext import Dispatcher,CommandHandler
import random

def four(update, context):
    update.message.reply_text("船员们划着桨，为马上要找到宝藏而激动不已。还记得之前逃走的那些海盗吗？在你们挖宝藏时要派人去放哨吗？\n输入 /yeswatch 来放哨\n输入 /nowatch 不放哨")

def add_handler(dp:Dispatcher):
    four_handler = CommandHandler('four', four)
    dp.add_handler(four_handler)
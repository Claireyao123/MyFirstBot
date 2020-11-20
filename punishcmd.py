from telegram.ext import Dispatcher,CommandHandler
import random


def punish(update, context):
    update.message.reply_text("欢迎来到命运的齿轮！你是不是又惹麻烦啦？看看规则吧！\n1. 输入 /startpunish 来开始转动命运的齿轮！\n2. 要听话！\n-----------------------\n希望你的级别平安无事！")

def add_handler(dp:Dispatcher):
    punish_handler = CommandHandler('punish', punish)
    dp.add_handler(punish_handler)
from telegram.ext import Dispatcher,CommandHandler
import random

def fishing(update, context):
    update.message.reply_text("欢迎来到钓鱼游戏！想知道附近的海域底下有什么吗？读读规则吧！\n1. 输入 /startfishing 来开始游戏\n2. 小心鲸鱼和鲨鱼！\n--------------------------\n玩的开心！")

def add_handler(dp:Dispatcher):
    fishing_handler = CommandHandler('fishing', fishing)
    dp.add_handler(fishing_handler)
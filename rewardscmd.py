from telegram.ext import Dispatcher,CommandHandler
import random

def rewards(update, context):
    update.message.reply_text("欢迎来到奖励大转盘！想在完成任务后获得奖励吗？看看规则吧！\n1. 输入 /startrewards 来开始抽奖!\n2. 记得完成任务哦！\n-----------------------\n玩的开心哦！")

def add_handler(dp:Dispatcher):
    rewards_handler = CommandHandler('rewards', rewards)
    dp.add_handler(rewards_handler)
from telegram.ext import Dispatcher,CommandHandler
import random

def treasure(update, context):
    update.message.reply_text("欢迎来到寻宝游戏！这是一场惊悚又危险追逐战，智慧，运气和勇气都是成功的关键！记得要避开海盗！读一读规则吧！\n1. 系统会自动给你分配即将要发生的事，做好心理准备！\n好的外表不一定有好的结果...\n2. 请输入 /starttreasure 来开始寻宝！\n-----------------------\n请开始你的航海之旅吧！祝你玩的开心！")

def add_handler(dp:Dispatcher):
    treasure_handler = CommandHandler('treasure', treasure)
    dp.add_handler(treasure_handler)

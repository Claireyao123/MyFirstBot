from telegram.ext import Dispatcher,CommandHandler
import random

def huntDinosaurs(update, context):
    update.message.reply_text("欢迎来到猎恐龙游戏🦕！在危机四伏的侏罗纪里你可以获得什么意想不到的惊喜呢？请看规则: \n1. 输入 /StartHuntDinosaurs 来开始游戏！\n2. 小心特暴龙！\n3. 开始收获 GP 和 XP 吧！\n--------------------------\n玩的开心哦！")

def add_handler(dp:Dispatcher):
    huntDinosaurs_handler = CommandHandler('huntDinosaurs', huntDinosaurs)
    dp.add_handler(huntDinosaurs_handler)
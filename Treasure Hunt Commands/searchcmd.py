from telegram.ext import Dispatcher,CommandHandler
import random

def search(update,context):
    if len(context.args) == 0 :
        update.message.reply_text("欢迎来到搜索游戏，这个游戏非常冒险，确定要继续吗？如果要，请看规则：\n1. 输入 /startsearch 来开始搜索 \n2. 系统会自动找地方让你去搜索哦！\n -------------------------\n玩的开心哦！")


def add_handler(dp:Dispatcher):
    search_handler = CommandHandler('search', search)
    dp.add_handler(search_handler)
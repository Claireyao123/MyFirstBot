from telegram.ext import Dispatcher,CommandHandler
import random

def dothecheck(update, context):
    update.message.reply_text("只见SCP-049以极高的速度移动过来并杀了你！\n哎，看了你对SCP的了解还不够！\n使用 /SCP 来练习练习吧！")

def add_handler(dp:Dispatcher):
    dothecheck_handler = CommandHandler('dothecheck', dothecheck)
    dp.add_handler(dothecheck_handler)
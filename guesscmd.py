from telegram.ext import Dispatcher,CommandHandler
import random
def guess(update, context):
    if len(context.args) == 0:
        update.message.reply_text("欢迎玩猜数字游戏，请在0-10之间猜一个数字吧！\nWelcome to Guess Number game, please guess between 0 and 10!")
    else: 
        number = int(context.args[0])
        update.message.reply_text("你输入的数字是%s"%number)


def add_handler(dp:Dispatcher):
    guess_handler = CommandHandler('guess', guess)
    dp.add_handler(guess_handler)


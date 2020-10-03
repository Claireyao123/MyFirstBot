from telegram.ext import Dispatcher,CommandHandler
import random
def guess(update, context):
    if len(context.args) == 0:
        update.message.reply_text(help())
    else:
        print(context.args)
        if context.args[0].isdigit():
            number = int(context.args[0])
            update.message.reply_text("you say %s"%number)
        else: 
            update.message.reply_text("你输入的%s不是数字"%context.args[0])
            

            
           


def add_handler(dp:Dispatcher):
    guess_handler = CommandHandler('guess', guess)
    dp.add_handler(guess_handler)


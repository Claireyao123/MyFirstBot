from telegram.ext import Dispatcher,CommandHandler
import random
result9 = ["大家喝的烂醉如泥，头沉沉的，于是各自回到了船舱里美美的睡了一觉。\n第二天是起早一点呢还是晚起一点呢？\n输入 /early 来早起\n输入 /late 来晚起"]

def drink(update, context):
    update.message.reply_text(random.choice(result9))

def add_handler(dp:Dispatcher):
    drink_handler = CommandHandler('drink', drink)
    dp.add_handler(drink_handler)
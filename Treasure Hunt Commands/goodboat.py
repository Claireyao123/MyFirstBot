from telegram.ext import Dispatcher,CommandHandler
import random
result1 = ["船已经准备好了，随时出击！现在要选水手了！\n输入 /goodman 来选择好水手👨.\n输入 /badman 来选择坏水手👨.", "你本以为这次出海会一帆风顺，但现实总变质，并不是你想要的样子。就在出发前一天晚上，你的船被人偷走了！你已经没有精力来继续航行了(你失去了 20HP 和 20AP)，回家继续撸你的猫吧！"]

def goodboat(update, context):
    update.message.reply_text(random.choice(result1))

def add_handler(dp:Dispatcher):
    goodboat_handler = CommandHandler('goodboat', goodboat)
    dp.add_handler(goodboat_handler)
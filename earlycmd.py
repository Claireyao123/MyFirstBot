from telegram.ext import Dispatcher,CommandHandler
import random
result10 = ["船员们精神饱满，激情四射。\n仔细一看，远处有一个小黑点，哦不！那是海盗船！幸好他们还没发现你们！\n现在要绕开还是战斗？\n输入 /away 来绕开\n输入 /fightP 来战斗", "船员们因为休息太少而无精打采，懒洋洋的。\n仔细一看，远处有个小黑点，哦不！那是海盗船！幸好他们还没发现你们！\n现在要绕开还是战斗？\n输入 /away 来绕开\n输入 /fightP 来战斗"]
def early(update, context):
    update.message.reply_text(random.choice(result10))

def add_handler(dp:Dispatcher):
    early_handler = CommandHandler('early', early)
    dp.add_handler(early_handler)
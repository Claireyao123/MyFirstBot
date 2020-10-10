from telegram.ext import Dispatcher,CommandHandler
import random

def starttreasure(update, context):
    update.message.reply_text("在一个风平浪静的早晨，你突然萌生了一个想法，出海寻宝！首先，你需要一搜船. \n输入 /badboat 来选择破船🚢. \n输入 /goodboat 来选择好船🚢")

def add_handler(dp:Dispatcher):
    starttreasure_handler = CommandHandler('starttreasure', starttreasure)
    dp.add_handler(starttreasure_handler)
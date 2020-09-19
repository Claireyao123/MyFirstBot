import random
from telegram.ext import CommandHandler
def punish(update, context):
    punish = ["啊喔！你丢掉了90XP! \nAh Oh! You lose 90XP！", "去死吧！你失去了80XP! \nBecause of your death, you lose 80XP!", "你没有得到任何惩罚！\nYou didn't get any punish!", "减掉100XP，今天不是你的幸运日哦！\nSubtract 100XP, it's not your day oh!"]
    context.bot.send_message(chat_id=update.effective_chat.id, text=random.choice(punish))

def add_dispatcher(dispatcher):
    punish_handler = CommandHandler('punish', punish)
    dispatcher.add_handler(punish_handler)
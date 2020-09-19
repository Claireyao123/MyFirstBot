from telegram.ext import CommandHandler
import random

def punish(update, context):
    punished = ["啊喔！你丢掉了90XP! \nAh Oh! You lose 90XP！", "去死吧！你失去了80XP! \nBecause of your death, you lose 80XP!", "你没有得到任何惩罚！\nYou didn't get any punish!", "减掉100XP，今天不是你的幸运日哦！\nSubtract 100XP, it's not your day oh!"]
    context.bot.send_message(chat_id=update.effective_chat.id, text=random.choice(punished))

def add_handler(dispatcher):
    start_handler = CommandHandler('punish', punish)
    dispatcher.add_handler(start_handler)
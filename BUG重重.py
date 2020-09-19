from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import os
import random
import rewards 
import punishes

def rewarded(update, context):
    reward = ["你得到了90XP, 还不错哦! \nYou got 90XP which was good enough! ", "你得到了40XP, 貌似有点少... \nYou got 40XP, seems a little bit little...", "哈哈，啥都没有！\nHa Ha! Nothing!", "运气也太好了吧？200XP? \nYou are so lucky? 200XP?", "100XP, 嫌少吗？\n100XP, less?"]
    context.bot.send_message(chat_id=update.effective_chat.id, text=random.choice(reward))
def punish(update, context):
    punished = ["啊喔！你丢掉了90XP! \nAh Oh! You lose 90XP！", "去死吧！你失去了80XP! \nBecause of your death, you lose 80XP!", "你没有得到任何惩罚！\nYou didn't get any punish!", "减掉100XP，今天不是你的幸运日哦！\nSubtract 100XP, it's not your day oh!"]
    context.bot.send_message(chat_id=update.effective_chat.id, text=random.choice(punished))
def read_file_as_str(file_path):
    # 判断路径文件存在
    if not os.path.isfile(file_path):
        raise TypeError(file_path + " does not exist")

    # 读取文件内容到all_the_text
    all_the_text = open(file_path).read()
    # print type(all_the_text)
    return all_the_text

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
    print(random.choice(rewarded))
 
TOKEN=read_file_as_str('TOKEN')

TOKEN = read_file_as_str('TOKEN2')
print (TOKEN)
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
rewards.add_handler(dispatcher)
punishes.add_handler(dispatcher)
updater.start_polling()

echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)

updater.start_polling()

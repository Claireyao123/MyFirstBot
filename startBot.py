from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import random
import os
import reward
import punish

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
    print(random.choice(reward))

TOKEN=read_file_as_str('TOKEN')

TOKEN = read_file_as_str('TOKEN2')
print (TOKEN)
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

reward.add_dispatcher(dispatcher)
punish.add_dispatcher(dispatcher)

updater.start_polling()

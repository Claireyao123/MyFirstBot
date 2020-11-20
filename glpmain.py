from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import os


def read_file_as_str(file_path):
    # 判断路径文件存在
    if not os.path.isfile(file_path):
        raise TypeError(file_path + " does not exist")

    # 读取文件内容到all_the_text
    all_the_text = open(file_path).read()
    # print type(all_the_text)
    return all_the_text

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=("""
    Hi everyone! My name is Claire!
    """))

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=("Sorry I don't understand this command..."))

TOKEN3=read_file_as_str('TOKEN3')

updater = Updater(token=TOKEN3, use_context=True)
me = updater.bot.get_me()
print(f"{me.username} start....")
dispatcher = updater.dispatcher
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)

updater.start_polling()
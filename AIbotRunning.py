from telegram.ext import Updater
from telegram.ext import CommandHandler, Dispatcher
from telegram.ext import MessageHandler, Filters
import os
import random
import whoareyou

msg = [
    """Hi, you can enter some commands in order to get my reponse :D""",
    """Oh, it seems that you don't know how to use my system. You can enter a command from the command list""",
    """Sorry I feel bad today, I don't want to talk... Please wait for 24 hours""",
    """I don't think you really enjoy talking to me, so why don't you try a command?""",
    """You are acting stupid, you want to or you are testing my system?""",
    """Have a nice day and... do you want to tell me some details about your day?""",
    """"""
    ]

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
    Hi! I'm a well-done AI bot! From now on, I'm your friend! 
    Now you can talk to me and play with me if you want! 
    /About Who I Am?
    /Emotion Tell me your feelings :D
"""))

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=random.choice(msg))

TOKEN2=read_file_as_str('TOKENai')

updater = Updater(token=TOKEN2, use_context=True)
me = updater.bot.get_me()
dispatcher = updater.dispatcher
print(f"{me.username} start....")
whoareyou.add_handler(dispatcher)
dispatcher = updater.dispatcher
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)

updater.start_polling()
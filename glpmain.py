from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import os
import dangercmd
import donate

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
    Hi! I am a robot created by Claire, use me if you want to learn something about an invasive species called Zebra Mussels!
    (Press the button to start visiting!)
    Also, you are welcome to our webite！Use this link：
    https://5fad4508177dc.site123.me/
    /Dangerous Click here to learn why Zebra Mussels are invasive species, why they are dangerous
    /donations Click here to donate something to our website！

    If you have questions, please send a message to this email: 
    cyao27@pickeringcollege.on.ca
    We will be happy to response you :)
    """))

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=("Sorry I don't understand this command, please press this button "))

TOKEN3=read_file_as_str('TOKEN3')

updater = Updater(token=TOKEN3, use_context=True)
me = updater.bot.get_me()
print(f"{me.username} start....")
dispatcher = updater.dispatcher
donate.add_handler(dispatcher)
dangercmd.add_handler(dispatcher)
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)

updater.start_polling()
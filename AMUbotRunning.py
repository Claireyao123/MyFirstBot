from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import os
import amongusRule
import AMUshop
import AMUcoins


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
Hi everyone! I am the Among Us Bot which created by Claire recently:
/AmongUs Start a Game / Check the Rules
/AmongUsShop Wanna buy something?
/AmongUsBank Check how much money you have
---------------------------
If you have questions, pls send to this email, we will be happy to response you :)
qianjiyao5@gmail.com
"""))

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=("这个我不知道怎么执行❓ \nSorry I don't understand this command..."))

TOKEN2=read_file_as_str('TOKEN2')

updater = Updater(token=TOKEN2, use_context=True)
me = updater.bot.get_me()
print(f"{me.username} start....")
dispatcher = updater.dispatcher
amongusRule.add_handler(dispatcher)
AMUshop.add_handler(dispatcher)
AMUcoins.add_handler(dispatcher)
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)

updater.start_polling()
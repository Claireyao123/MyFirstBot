from telegram.ext import Dispatcher
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters
from telegram.ext import CommandHandler
import random
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
    context.bot.send_message(chat_id=update.effective_chat.id, text="大家好！我是一个每天无所事事的咸鱼，总想找人聊天，我自己会不断升级的！升级详情请看我的名字哦！\n(声明：有时候翻译不准是那个 Google Translate 的错，跟我没关系哦！)\n---------------------------\n/guess 猜数字游戏📖 \n/search 搜索游戏🔍\n/treasure 寻宝游戏🏴‍☠️\n祝大家玩的开心！")

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

TOKEN=read_file_as_str('TOKEN2')

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)

updater.start_polling()
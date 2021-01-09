from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import os
import guesscmd
import searchcmd
import treasurecmd 
import huntDinosaurscmd
import StartHuntDinosaurscmd
import rewardscmd
import startrewardscmd
import punishcmd
import startpunishcmd
import killbotcmd
import fishing
import historycmd
import CanadaHistoryChinese
import ChinaHistoryChinese
import amongusRule
import coins
import gif
import info

gifSTART = 'https://images.huffingtonpost.com/2014-03-21-fish.gif'

def read_file_as_str(file_path):
    # 判断路径文件存在
    if not os.path.isfile(file_path):
        raise TypeError(file_path + " does not exist")

    # 读取文件内容到all_the_text
    all_the_text = open(file_path).read()
    # print type(all_the_text)
    return all_the_text

def start(update, context):
    update.message.reply_animation(gifSTART)
    context.bot.send_message(chat_id=update.effective_chat.id, text=("""
    大家好！我是一个每天无所事事的咸鱼，总想找人聊天。我自己也会不断升级的，升级详情请看我的名字！
    有的时候翻译不准是 Google Translate 的错，跟我没关系！

    ------------------------------------------
    /guess 猜数字游戏📖
    /search 搜索游戏🔍
    /treasure 寻宝游戏🏴‍☠️
    /huntDinosaurs 猎恐龙游戏🦕
    /rewards 奖励大转盘🎁
    /punish 命运的齿轮⚙️
    /history 历史辅导📃
    /fishing 钓鱼游戏🎣
    /gif 发送有意思的动图😂
    /info 发送信息的详情🔎

    ------------------------------------------

    如果不喜欢我可以使用 /killbot ，但是本机器人极其不建议使用这个命令!!!

    祝大家玩的开心！

    ———————————————————————————————————————————
    Hello Everyone! 
    I'm a lovely salt fish, please talk to me! I will update everytime I added a command, so watch out for my name!
    (My English is not perfect because of Google Translate, sorry for that!)

    ------------------------------------------
    /guess Guess Number Game 📖
    /search Search Game 🔍
    /treasure Treasure Hunt Game 🏴‍☠️
    /fishing Fishing Game 🎣
    /history History Helping 📃
    /rewards Random Rewards 🎁
    /punish Random Punishes 😈
    /gif Sending funny gifs 😂
    /info Sending Details About A Message 🔎

    -----------------------------------------

    If you dislike me, you can use /killbot , but please don't !!!

    Hope you enjoy!
    """))

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=("你看你已经累糊涂了，快去喝杯咖啡☕️休息一下吧！"))

TOKEN=read_file_as_str('TOKEN')

updater = Updater(token=TOKEN, use_context=True)
me = updater.bot.get_me()
print(f"{me.username} start...")
dispatcher = updater.dispatcher
gif.add_handler(dispatcher)
info.add_dispatcher(dispatcher)
amongusRule.add_handler(dispatcher)
coins.add_handler(dispatcher)
guesscmd.add_handler(dispatcher)
searchcmd.add_handler(dispatcher)
treasurecmd.add_handler(dispatcher)
huntDinosaurscmd.add_handler(dispatcher)
StartHuntDinosaurscmd.add_handler(dispatcher)
rewardscmd.add_handler(dispatcher)
punishcmd.add_handler(dispatcher)
startrewardscmd.add_handler(dispatcher)
startpunishcmd.add_handler(dispatcher)
killbotcmd.add_handler(dispatcher)
fishing.add_handler(dispatcher)
historycmd.add_handler(dispatcher)
CanadaHistoryChinese.add_handler(dispatcher)
ChinaHistoryChinese.add_handler(dispatcher)

commands = guesscmd.get_command()
bot = updater.bot
bot.set_my_commands(commands)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)

updater.start_polling()
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import os
import guesscmd
import searchcmd
import startsearchcmd
import treasurecmd
import starttreasurecmd
import badboatcmd
import goodboat
import badmancmd
import goodmancmd
import fastcmd
import slowcmd
import yeswalkcmd
import nowalkcmd
import fightcmd
import runcmd
import drinkcmd
import restcmd
import dancecmd
import earlycmd
import latecmd
import fightPcmd
import awaycmd
import happycmd
import checkcmd
import threecmd
import fourcmd
import yeswatchcmd
import nowatchcmd
import islandcmd
import boatcmd
import huntDinosaurscmd
import StartHuntDinosaurscmd
import rewardscmd
import startrewardscmd
import punishcmd
import startpunishcmd
import killbotcmd


def read_file_as_str(file_path):
    # 判断路径文件存在
    if not os.path.isfile(file_path):
        raise TypeError(file_path + " does not exist")

    # 读取文件内容到all_the_text
    all_the_text = open(file_path).read()
    # print type(all_the_text)
    return all_the_text

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="大家好！我是一个每天无所事事的咸鱼，总想找人聊天，我自己会不断升级的！升级详情请看我的名字哦！\n(声明：有时候翻译不准是那个 Google Translate 的错，跟我没关系哦！)\n---------------------------\n/guess 猜数字游戏📖 \n/search 搜索游戏🔍\n/treasure 寻宝游戏🏴‍☠️\n/huntDinosaurs 猎恐龙游戏🦕\n/rewards 奖励大转盘🎁\n/punish 命运的齿轮😈\n\n\n祝大家玩的开心！")

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=("不要瞎说！用 /start 来看看我的功能吧"))

TOKEN=read_file_as_str('TOKEN')

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher
guesscmd.add_handler(dispatcher)
searchcmd.add_handler(dispatcher)
startsearchcmd.add_handler(dispatcher)
treasurecmd.add_handler(dispatcher)
starttreasurecmd.add_handler(dispatcher)
badboatcmd.add_handler(dispatcher)
goodboat.add_handler(dispatcher)
badmancmd.add_handler(dispatcher)
goodmancmd.add_handler(dispatcher)
fastcmd.add_handler(dispatcher)
slowcmd.add_handler(dispatcher)
yeswalkcmd.add_handler(dispatcher)
nowalkcmd.add_handler(dispatcher)
fightcmd.add_handler(dispatcher)
runcmd.add_handler(dispatcher)
drinkcmd.add_handler(dispatcher)
restcmd.add_handler(dispatcher)
dancecmd.add_handler(dispatcher)
earlycmd.add_handler(dispatcher)
latecmd.add_handler(dispatcher)
fightPcmd.add_handler(dispatcher)
awaycmd.add_handler(dispatcher)
happycmd.add_handler(dispatcher)
checkcmd.add_handler(dispatcher)
threecmd.add_handler(dispatcher)
fourcmd.add_handler(dispatcher)
yeswatchcmd.add_handler(dispatcher)
nowatchcmd.add_handler(dispatcher)
islandcmd.add_handler(dispatcher)
boatcmd.add_handler(dispatcher)
huntDinosaurscmd.add_handler(dispatcher)
StartHuntDinosaurscmd.add_handler(dispatcher)
rewardscmd.add_handler(dispatcher)
punishcmd.add_handler(dispatcher)
startrewardscmd.add_handler(dispatcher)
startpunishcmd.add_handler(dispatcher)
killbotcmd.add_handler(dispatcher)
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)

updater.start_polling()
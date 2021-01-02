from datetime import datetime,timedelta
from telegram.ext import Dispatcher,CommandHandler,Filters
from telegram import BotCommand
import config 
import random

def FP(update,context):
    gifs = ['https://irtfyblog.files.wordpress.com/2015/04/fall_ice_fail.gif','']
    gif = random.choice(gifs)
    update.message.reply_animation(gif,caption="hi")

def add_handler(dp:Dispatcher):
    FPgif_handler = CommandHandler('PuddleGIF', FP)
    dp.add_handler(FPgif_handler)

def get_command():
    return [BotCommand('FPgif',FP)]
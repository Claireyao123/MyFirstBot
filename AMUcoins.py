import random
from datetime import datetime,timedelta
from telegram.ext import Dispatcher,CommandHandler

AMU = {}

def check_user(chatid,user):
    uid = user.id
    first_name = user.first_name
    if not chatid in AMU.keys():
        AMU[chatid] = {}
    if not uid in AMU[chatid].keys():
        AMU[chatid][uid] = {'name':first_name,'AMU':0,'count':0,'dailytime':datetime.now()}

def show_user(chatid,user):
    uid = user.id
    check_user(chatid,user)
    #  老房东(10):200
    return f"{AMU[chatid][uid]['name']}({AMU[chatid][uid]['count']}):{AMU[chatid][uid]['AMU']}"

def add_coins(chatid,user,c):
    check_user(chatid,user)
    uid = user.id
    AMU[chatid][uid]['AMU'] += c

def add_count(chatid,user):
    check_user(chatid,user)
    uid = user.id
    AMU[chatid][uid]['count'] += 1

def daily(chatid,user):
    check_user(chatid,user)
    uid = user.id
    if datetime.now() > AMU[chatid][uid]['dailytime']:
        c = random.randint(1,100)
        AMU[chatid][uid]['AMU'] += c
        AMU[chatid][uid]['dailytime'] = datetime.now() + timedelta(minutes=5)
        return c
    else:
        return 0

def get_AMU(update, context):
    chatid = update.effective_chat.id
    user = update.effective_user
    check_user(chatid,user)
    update.message.reply_text(f"{show_user(chatid,user)}")

def add_handler(dp:Dispatcher):
    dp.add_handler(CommandHandler('AmongUsBank', get_AMU))
import random
from datetime import datetime,timedelta
from telegram.ext import Dispatcher,CommandHandler
from telegram import Animation
import config
import gif

# {
#     chatid: {
#         uid :{
#             'name': first_name,
#             'coins': 123,
#             'count': 0,
#             'dailytime' : time
#         }
#     }
# }

coins = config.CONFIG["coins"]

print(f"init coins:{coins}")

def save():
    config.CONFIG["coins"] = coins
    config.save_config()

def check_user(chatid,user):
    uid = str(user.id)
    first_name = user.first_name
    if not chatid in coins.keys():
        coins[chatid] = {}
    if not uid in coins[chatid].keys():
        coins[chatid][uid] = {'name':first_name,'coins':0,'count':0}
        set_dailytime(chatid,uid,datetime.now())

def show_user(chatid,user):
    uid = str(user.id)
    check_user(chatid,user)
    #  老房东(10):200
    return f"{coins[chatid][uid]['name']}({coins[chatid][uid]['count']}):{coins[chatid][uid]['coins']}"

def add_coins(chatid,user,c):
    check_user(chatid,user)
    uid = str(user.id)
    coins[chatid][uid]['coins'] += c
    print(f"add_coins:{coins}")
    save()

def add_count(chatid,user):
    check_user(chatid,user)
    uid = str(user.id)
    coins[chatid][uid]['count'] += 1

def get_dailytime(chatid,uid):
    date_string = coins[chatid][uid]['dailytime']
    return  datetime.strptime(date_string, "%H:%M:%S, %d %B, %Y")

def set_dailytime(chatid,uid,time):
    coins[chatid][uid]['dailytime'] = time.strftime("%H:%M:%S, %d %B, %Y")
    
def daily(chatid,user):
    check_user(chatid,user)
    uid = str(user.id)
    if datetime.now() > get_dailytime(chatid,uid):
        c = random.randint(1,100)
        coins[chatid][uid]['coins'] += c
        time = datetime.now() + timedelta(minutes=5)
        set_dailytime(chatid,uid,time)
        save()
        return c
    else:
        return 0

def get_coins(update, context):
    chatid = str(update.effective_chat.id)
    user = update.effective_user
    check_user(chatid,user)
    animation = Animation("CgACAgEAAxkBAAIED1_naCvPkSF70_YFSBOLFqR3HdJrAALwAANZ9ThHLVPTI945GIIeBA","AgAD8AADWfU4Rw",220,221,5)
    update.message.reply_animation(animation, caption="hi")
    # update.message.reply_animation(animation=open('/Users/qianjiyao/work/MyFirstBot/image/dino.mp4',"rb"))
def add_handler(dp:Dispatcher):
    dp.add_handler(CommandHandler('coins', get_coins))
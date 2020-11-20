from telegram.ext import Dispatcher,CommandHandler,CallbackQueryHandler
from telegram import InlineKeyboardMarkup,InlineKeyboardButton, BotCommand
import random
from datetime import datetime,timedelta
import coins

smallButton = InlineKeyboardButton('比10小一点',callback_data='guess:small')
bigButton = InlineKeyboardButton('比10大一点',callback_data='guess:big')
sumButton = InlineKeyboardButton('看看结果',callback_data='guess:sum')
dailyButton = InlineKeyboardButton('获得奖励',callback_data='guess:daily')

gamekb = InlineKeyboardMarkup([[bigButton,smallButton,sumButton]])

joinButton = InlineKeyboardButton('加入游戏',callback_data='guess:join')
startButton = InlineKeyboardButton('开始游戏',callback_data='guess:start')

startkb = InlineKeyboardMarkup([[joinButton,startButton,dailyButton]])

timer = 0

# { 
#  chatid: {
#    h:"", 
#    p:{
#       user:d
#    }
# }
games = {}

def check_chatid(chatid):
    if not chatid in games.keys():
        games[chatid]={
            "h":"",
            "p":{}
            }

def getHist(chatid):
    return games[chatid]['h']

def setHist(chatid,res):
    h = games[chatid]['h']
    if len(h) > 10:
        h = h[:9] + res
    else:
        h += res
    games[chatid]['h'] = h

def getNumber():
    endNumber = 0
    msg = ""
    for _i in range(3):
        rnumber = random.randint(1,6)
        endNumber += rnumber
        msg += "%s "%rnumber
    msg += "=%s" % endNumber
    return [endNumber,msg]

def sumGame(chatid):
    number,msg = getNumber()
    users = games[chatid]["p"]
    game = 'x'
    if number >= 11:
        game = 'd'
    setHist(chatid,game)
    for u in users.keys():
        if users[u] == '':
            users[u] = '？？？你没选？？？'
        elif users[u] == game:
            c = random.randint(0,10)
            coins.add_coins(chatid,u,c)
            users[u] = f'Yes! 你赢取了{c}个金币'
            coins.add_count(chatid,u)
        else:
            c = random.randint(0,10) * -1
            coins.add_coins(chatid,u,c)
            users[u] = f'Noo!你输掉了{c}个金币'
            coins.add_count(chatid,u)
    msg += "\n%s"%getUsers(users)
    return msg 

def getUsers(users):
    msg = ""
    for u in users.keys():
        print(u)
        msg += "%s:%s\n"%(u.first_name,users[u])
    return msg

def guess(update, context):
    global timer
    chatid = update.effective_chat.id
    check_chatid(chatid)
    timer = datetime.now() + timedelta(seconds=5)
    update.message.reply_text("开始游戏🎮！",reply_markup=startkb)

def buttonCallback(update, context):
    global games,timer
    query = update.callback_query 
    chatid = update.effective_chat.id
    user = update.effective_user
    check_chatid(chatid)
    users = games[chatid]["p"]
    print(f"s:{games}")
    msg = getUsers(users) + "\n\n" + getHist(chatid)
    if query.data == 'guess:join':
        query.answer("加入游戏")
        users[update.effective_user] = ""
        query.edit_message_text(msg,reply_markup=startkb)
        return
    elif query.data == "guess:daily":
        c = coins.daily(chatid,user)
        if c == 0:
            query.answer("别着急，每五分钟只能打一次卡",show_alert=True)
        else:
            query.answer(f"打卡成功了，你获得了{c}个金币",show_alert=True)
    elif query.data == 'guess:start':
        timenow = datetime.now()
        if timenow > timer:
            query.answer("开始游戏！")
            query.edit_message_text(msg,reply_markup=gamekb)
            timer = datetime.now()+timedelta(seconds=5)
        else:
            query.answer("冷静！还没到五秒！",show_alert=True)
    elif query.data == 'guess:big':
        if users == {}:
            return
        query.answer("你选择了大")
        users[update.effective_user] = "d"
        query.edit_message_text(msg,reply_markup=gamekb)
    elif query.data == 'guess:small':
        if users == {}:
            return
        query.answer("你选择了小")
        users[update.effective_user] = "x"
        query.edit_message_text(msg,reply_markup=gamekb)
    elif query.data == 'guess:sum':
        timenow = datetime.now()
        if timenow > timer:
            query.answer("结算开始")
            msg = sumGame(chatid)+ "\n\n" +getHist(chatid)
            query.edit_message_text(msg)
            users = {}
        else:
            query.answer("冷静！还没到五秒！",show_alert=True)
    games[chatid]["p"] = users
    print(f"e:{games}")

def get_command():
    return [BotCommand('guess', '试试运气')]

def add_handler(dp:Dispatcher):
    dp.add_handler(CommandHandler('guess', guess))
    dp.add_handler(CallbackQueryHandler(buttonCallback,pattern="^guess:[A-Za-z0-9_]*"))
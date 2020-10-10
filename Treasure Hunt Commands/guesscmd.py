from telegram.ext import Dispatcher,CommandHandler
import random
rnumber = random.randint(1,99)
ren = {}
games = {}
def guess(update, context):
    chatid = update.message.chat.id
    global rnumber 
    if not (chatid in games):
        games[chatid] = {'rnamber':random.randint(1,99), "member":{} }
    print (games)
    if len(context.args) == 0:
        update.message.reply_text("欢迎来到猜数字游戏！请看规则: \n请输入 /guess (1-100之间的一个数字)，系统会提示你大了，小了或猜中了。每一次猜中就会重新调整数字! \n---------------------------\n你目前在 %s 玩游戏"%(chatid))
    else:
        global rnumber
        name = update.message.from_user.first_name
        if context.args[0].isdigit():
            number = int(context.args[0])
            fname = update.message.from_user.first_name
            if fname in games[chatid]['member']:
                games[chatid]['member'][fname] += 1
            else: 
                games[chatid]['member'][fname] = 1
            if number == games[chatid]["rnamber"]:
                update.message.reply_text("哇！厉害呀！你居然只用了%s次就猜中了这个超级稀有的数字啦！这 500XP 是你应得的奖励，幸运之神！\n系统已经刷新了数字，想要重新玩就输入 /guess 吧！"%games[chatid]['member'][fname])
                games[chatid]["rnamber"] = random.randint(1,99)
                games[chatid]['member'] = {}
            elif number < games[chatid]['rnamber']: 
                update.message.reply_text("啊哦！你好像猜小了一点，快点重猜吧！\n你已经猜了%s次了"%games[chatid]['member'][fname])
                games[chatid]['member'][fname] += 1
            elif number > games[chatid]['rnamber']: 
                update.message.reply_text("啊呀！你好像猜大了一点，快点重猜吧！\n你已经猜了%s次了"%games[chatid]['member'][fname])
                games[chatid]['member'][fname] += 1
        else: 
            update.message.reply_text("不不不！你输入的 %s 不是数字耶，读一读规则然后重猜吧！"%context.args[0])
            
def add_handler(dp:Dispatcher):
    guess_handler = CommandHandler('guess', guess)
    dp.add_handler(guess_handler)


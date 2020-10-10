from telegram.ext import Dispatcher,CommandHandler
import random
result17 = ["厉害呀！幸运之神！你居然得到了 200XP ! 古今少有啊！", "emm... 40XP 有一点是一点啦！", "运气不错！得到了 90XP !", "漂亮！啥都没有！"]

def startrewards(update, context):
    update.message.reply_text(random.choice(result17))

def add_handler(dp:Dispatcher):
    startrewards_handler = CommandHandler('startrewards', startrewards)
    dp.add_handler(startrewards_handler)
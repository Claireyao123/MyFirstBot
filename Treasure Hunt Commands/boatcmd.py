from telegram.ext import Dispatcher,CommandHandler
import random

def boat(update, context):
    update.message.reply_text("你和你的船员们把财宝带上了船并回到了港口！\n你成功了！现在你是独一无二的优秀船长！太厉害啦！！！\n这 15000XP 50AP 200GP 是从宝箱里取出来的奖励！好好使用它吧！\n寻宝游戏圆满结束啦！使用 /start 来看看玩点别的什么吧！")

def add_handler(dp:Dispatcher):
    boat_handler = CommandHandler('boat', boat)
    dp.add_handler(boat_handler)
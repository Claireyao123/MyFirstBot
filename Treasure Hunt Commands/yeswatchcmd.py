from telegram.ext import Dispatcher,CommandHandler
import random
result14 = ["幸亏有人放哨，你们及时发现了海盗，把海盗打跑了以后你们取出了埋在沙子里的宝箱！\n现在要在岛上过夜还是会船？\n输入 /island 在岛上过夜\n输入 /boat 船上过夜", "你们过去一看，放哨的人竟然被杀了！这时，海盗从四面八方冲了出来，把所有人绑架到了船上"]

def yeswatch(update, context):
    update.message.reply_text(random.choice(result14))

def add_handler(dp:Dispatcher):
    yeswatch_handler = CommandHandler('yeswatch', yeswatch)
    dp.add_handler(yeswatch_handler)
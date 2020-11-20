from telegram.ext import Dispatcher,CommandHandler
import random
result2 = ["水手们骚动不安，不过还是很听话的\n恭喜你，你成功出海了！不过危险还在后面呢！\n选择一个速度(速度越快到达时间越快，不过船散架的可能性越大)\n输入 /fast 来开的更快一些\n输入 /slow 来减慢速度", "水手们嫌你指挥不好，半夜逃走了。你虽然历经千辛万苦买到了船，却还是失败了，回家休息吧！(由于生气，你失去了 10HP)"]

def badman(update, context):
    update.message.reply_text(random.choice(result2))

def add_handler(dp:Dispatcher):
    badman_handler = CommandHandler('badman', badman)
    dp.add_handler(badman_handler)
from telegram.ext import Dispatcher,CommandHandler
import random
result4 = ["你的船开的太快了，已经散架了，你和所有船员都葬身海底，此生无遗憾...", "你的船快到变成了磁悬浮船，飞离了水面！船员们被吹得东倒西歪，因此对你很生气，有暴乱的可能...\n为了鼓舞人心，你想不想带着船员去甲板上散步? \n输入 /yeswalk 表示同意\n输入 /nowalk 表示不同意","船开的飞快，船员们都非常兴奋，你干的非常不错\n为了鼓舞人心，你想不想带着船员去甲板上散步? \n输入 /yeswalk 表示同意\n输入 /nowalk 表示不同意" ]

def fast(update, context):
    update.message.reply_text(random.choice(result4))

def add_handler(dp:Dispatcher):
    fast_handler = CommandHandler('fast', fast)
    dp.add_handler(fast_handler)
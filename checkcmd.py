from telegram.ext import Dispatcher,CommandHandler
import random
result13 = ["大家一起齐心协力的把方位计算好了。前方发现小岛啦！！！你兴奋不已。\n要准备几条船呢？\n输入 /three 来准备3条船\n输入 /four 来准备4条船", "弄着弄着所有人就睡着了，船被风吹到了百慕大三角，所有人都葬身海底..."]

def check(update, context):
    update.message.reply_text(random.choice(result13))

def add_handler(dp:Dispatcher):
    check_handler = CommandHandler('check', check)
    dp.add_handler(check_handler)
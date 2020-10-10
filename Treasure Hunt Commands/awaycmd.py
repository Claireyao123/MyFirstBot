from telegram.ext import Dispatcher,CommandHandler
import random
result12 = ["你的船右满舵，暂时躲开了海盗的攻击，不过你们迷失了方向，所以只好发出求救信号。到底有没有人能接到呢？", "你把船开到了最快，结果散架了，所有人直接归西...", "唉，你逃的还是不够快，海盗的加农炮把你的船打漏了，所有人葬身海底..."]

def away(update, context):
    update.message.reply_text(random.choice(result12))

def add_handler(dp:Dispatcher):
    away_handler = CommandHandler('away', away)
    dp.add_handler(away_handler)
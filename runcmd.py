from telegram.ext import Dispatcher,CommandHandler
import random
result8 = ["幸好你们逃的够快，很快把海怪给甩了，不过你们的藏宝图在逃跑过程中丢失了，也只好原路返回到港口", "你已经把船开到了全速，结果散架了...", "唉，你们逃的还是不够快，海怪到底是追上你们了，你们被吃了"]

def run(update, context):
    update.message.reply_text(random.choice(result8))

def add_handler(dp:Dispatcher):
    run_handler = CommandHandler('run', run)
    dp.add_handler(run_handler)
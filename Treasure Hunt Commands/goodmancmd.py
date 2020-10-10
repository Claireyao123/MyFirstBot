from telegram.ext import Dispatcher,CommandHandler
import random
result3 = ["你不愧是幸运之子，你挑选的水手都非常的听话能干\n恭喜你通过了第一个考验，现在来选择一个速度(速度越快到达时间越快，不过船散架的可能性越大)\n输入 /fast 来开的更快一些\n输入 /slow 来减慢速度", "你万万没想到水手们居然被其他人买通了！你还是太大意了！放弃出海吧！(由于惊讶而失去了 25HP )"]
def goodman(update, context):
    update.message.reply_text(random.choice(result3))

def add_handler(dp:Dispatcher):
    goodman_handler = CommandHandler('goodman', goodman)
    dp.add_handler(goodman_handler)
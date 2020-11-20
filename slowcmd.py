from telegram.ext import Dispatcher,CommandHandler
import random
result5 = ["让我们荡起双桨，小船儿推开波浪...你虽然开的很慢，但是水手们光顾着喝酒，没注意到\n为了鼓舞人心，你想不想带着船员去甲板上散步? \n输入 /yeswalk 表示同意\n输入 /nowalk 表示不同意", "你发现水手们都朝你投去抱怨都眼光，还好最近没有暴乱都迹象...\n为了鼓舞人心，你想不想带着船员去甲板上散步? \n输入 /yeswalk 表示同意\n输入 /nowalk 表示不同意","水手们开始抱怨太慢，你不得不把速度提了起来，结果船散架了，大家都落入了水中...愚民啊！为什么连这种危险都想不到？就这样，你带着这个念头沉入了海底"]
def slow(update, context):
    update.message.reply_text(random.choice(result5))

def add_handler(dp:Dispatcher):
    slow_handler = CommandHandler('slow', slow)
    dp.add_handler(slow_handler)
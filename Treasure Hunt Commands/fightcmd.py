from telegram.ext import Dispatcher,CommandHandler
import random
result7 = ["不愧是久经沙场的老水手，大家齐心协力的把海怪打跑了！你用它的触角给每个人都做了一个辟邪的法宝，以后遇到危险的时候可以用! \n结下来要做什么？\n输入 /drink 来喝酒庆祝\n输入 /dance 来跳舞庆祝\n输入 /rest 来休息", "你们奋力抵抗，却还是被命运惩罚了，不过好在你准备了足够都救生船，使得所有人逃过一劫。你的航海生涯结束了...", "只见海怪用力一劈，整艘船断成了两截，所有人直接归西..."]

def fight(update, context):
    update.message.reply_text(random.choice(result7))

def add_handler(dp:Dispatcher):
    fight_handler = CommandHandler('fight', fight)
    dp.add_handler(fight_handler)
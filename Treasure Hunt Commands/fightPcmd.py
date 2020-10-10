from telegram.ext import Dispatcher,CommandHandler
import random
result11 = ["在一片喧杂的叫喊声中海盗们登上了你的船。在慌乱之际，突然，一把长刀刺入了你的胸膛。你只来得及看最后一眼你的船，便停止了呼吸...希望你的船员能找到宝藏！", "你的大炮打坏了海盗船，你们边喝酒边幸灾乐祸的看着海盗船下沉，海盗们挣扎着逃走了几个人。看来海盗也没你想像的那么厉害嘛！你犯了一个致命的错误...\n接下来是狂欢还是规划路线？\n输入 /happy 来狂欢\n输入 /check 来规划路线", "战斗的号角已吹响，你在最前面猛砍猛杀，船员们气势高涨！海盗们还是逃走了几个，不过你也没多想！你犯了一个致命的错误...\n接下来怎么办？\n输入 /happy 来狂欢\n输入 /check 来规划路线"]

def fightP(update, text):
    update.message.reply_text(random.choice(result11))

def add_handler(dp:Dispatcher):
    fightP_handler = CommandHandler('fightP', fightP)
    dp.add_handler(fightP_handler)

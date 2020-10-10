from telegram.ext import Dispatcher,CommandHandler
import random

def hydrochloricAcid(update, context): 
    update.message.reply_text("可以！SCP-682被你制服了！厉害啊！\n看来你对SCP基金会还是有一定了解的！\n解说：\nSCP-682在盐酸里会全身无力，并无法伤害人类。\n你得到了 700XP 作为帮助收容的奖励!回到 /SCP 试试别的SCP吧！")


def add_handler(dp:Dispatcher):
    hydrochloricAcid_handler = CommandHandler('hydrochloricAcid', hydrochloricAcid)
    dp.add_handler(hydrochloricAcid_handler)
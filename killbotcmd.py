from telegram.ext import Dispatcher,CommandHandler
import random

msg = [
    """一番搏斗后，大家看到 Salted Fish 拿着一把带血的刀扬长而去。。。\n R.I.P""",
    """你奋力将Salted Fish 打倒并送走，但是受了重伤，被直接反扑后归西。。。""",
    """你将一把尖刀插入了 Salted Fish ，赢得了这场战斗的胜利！""",
    """你不忍心杀死这么一个可爱的程序，于是放弃了打斗的念头""",
    """你对 Salted Fish 越发不满，可是打不过，于是你灰溜溜的逃走了。。。""",
    """你根本不知道 Salted Fish 在哪里，找了一整天后放弃了。。。""",
    """你气的七窍生烟，直接归西"""
]

def killbot(update, context):
    update.message.reply_text(random.choice(msg))

def add_handler(dp:Dispatcher):
    killbot_handler = CommandHandler('killbot', killbot)
    dp.add_handler(killbot_handler)
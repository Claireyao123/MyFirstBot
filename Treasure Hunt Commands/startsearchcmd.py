from telegram.ext import Dispatcher,CommandHandler
import random
searches = ["有一天你决定去公园，在地上看到了一个钱包，你把它捡了起来并取走了所有的钱 (你获得了 100 GP)。一年后你被逮捕了！", "有一天你决定去海底基地，由于氧气没带够而死掉了。", "有一天你决定去海底基地，不过由于没带通行证而被赶了出来。", "有一天你决定去海底基地，你发现了两个稀有物种，你获得了 200XP 作为奖励。", "有一天你决定去科技馆，发现了一个传送门，你传送到了侏罗纪结果被恐龙咬死了", "有一天你决定去科技馆，发现了一个传送门，你传送到了侏罗纪，你带回了一个恐龙蛋并得到了 900XP 作为奖励！", "有一天你决定去沙滩上走走，结果你被一块石头绊倒了，你花了 70GP 治疗费", "有一天你决定去医院看看，结果诈尸了，你被吓出了精神病", "有一天你决定去野生动物园看看，你花了 10GP 来买门票，你看动物看的很开心", "有一天你决定去潜水，结果被海浪冲跑了。当你醒来时发现你降回了1级！哦不！以后不要潜水了！"]

def startsearch(update, context): 
 update.message.reply_text(random.choice(searches))

def add_handler(dp:Dispatcher):
    startsearch_handler = CommandHandler('startsearch', startsearch)
    dp.add_handler(startsearch_handler)

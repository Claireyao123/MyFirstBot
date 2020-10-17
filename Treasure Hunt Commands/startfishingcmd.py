from telegram.ext import Dispatcher,CommandHandler
import random
result30 = ["有一天你决定去钓鱼，换上靴子并来到了河边。可是你居然忘带水桶了！只好回家...", "有一天你决定去钓鱼，换上靴子并来到了河边。可是你居然忘带鱼饵了！只好回家...", "有一天你决定去钓鱼，换上靴子并来到了河边。只见你一甩竿，一条三文鱼越出水面！\n你获得了 80XP ", "有一天你决定去钓鱼，换上靴子并来到了河边。只见你一甩竿，两条三文鱼越出了水面！\n你获得了 160XP ", "有一天你决定去钓鱼，换上靴子并来到了河边。只见你一甩竿，一条鳟鱼越出了水面！\n你得到了 40XP ", "有一天你决定去钓鱼，换上靴子并来到了河边。只见你一甩竿，两条鳟鱼越出了水面！\n你得到了 80XP ", "有一天你决定去钓鱼，换上靴子并来到了河边。只见你一甩竿，一个黑色的物体飞出了水面，竟然是一张银行卡！你把它交给了警察并得到了 100XP 作为诚实者的奖励", "有一天你决定去钓鱼，换上靴子并来到了河边。只见你一甩竿，一个庞然大物飞出了水面，那竟然是一条小虎鲨！你是怎么做到的？\n你获得了 200XP ", "有一天你决定去钓鱼，换上靴子并来到了河边。只见你一甩竿，结果被一个东西拖下了水，是一条鲸鱼！\n傍晚，你浑身湿淋淋的，拖着疲惫的身子回家了...", "你跳到那个庞然大物上用长刀乱砍，终于把它砍晕了。那竟然是条鲸鱼！！太厉害啦！\n你得到了 550XP ", "你拼命挣扎着用鱼钩把一个东西拖上了船，那是一条虎鲨！\n你得到了 500XP "]

def startfishing(update, context):
    update.message.reply_text(random.choice(result30))

def add_handler(dp:Dispatcher):
    startfishing_handler = CommandHandler('startfishing', startfishing)
    dp.add_handler(startfishing_handler)
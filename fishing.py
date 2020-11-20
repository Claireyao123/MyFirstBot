from telegram.ext import Dispatcher,CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardMarkup,InlineKeyboardButton
import random

result30 = [
    """有一天你决定去钓鱼，换上靴子并来到了河边。可是你居然忘带水桶了！只好回家...""", 
    """有一天你决定去钓鱼，换上靴子并来到了河边。可是你居然忘带鱼饵了！只好回家...""", 
    """有一天你决定去钓鱼，换上靴子并来到了河边。只见你一甩竿，一条三文鱼越出水面！
    你获得了 80 S币""", 
    """有一天你决定去钓鱼，换上靴子并来到了河边。只见你一甩竿，两条三文鱼越出了水面！
    你获得了 160 S币 """, 
    """有一天你决定去钓鱼，换上靴子并来到了河边。只见你一甩竿，一条鳟鱼越出了水面！
    你得到了 40 S币 """, 
    """有一天你决定去钓鱼，换上靴子并来到了河边。只见你一甩竿，两条鳟鱼越出了水面！
    你得到了 80 S币 """, 
    """有一天你决定去钓鱼，换上靴子并来到了河边。只见你一甩竿，一个黑色的物体飞出了水面，竟然是一张银行卡！你把它交给了警察并得到了 100 S币 作为诚实者的奖励""", 
    """有一天你决定去钓鱼，换上靴子并来到了河边。只见你一甩竿，一个庞然大物飞出了水面，那竟然是一条小虎鲨！你是怎么做到的？
    你获得了 200 S币 """, 
    """有一天你决定去钓鱼，换上靴子并来到了河边。只见你一甩竿，结果被一个东西拖下了水，是一条鲸鱼！
    傍晚，你浑身湿淋淋的，拖着疲惫的身子回家了...""", 
    """你跳到那个庞然大物上用长刀乱砍，终于把它砍晕了。那竟然是条鲸鱼！！太厉害啦！
    你得到了 550 S币 """, 
    """你拼命挣扎着用鱼钩把一个东西拖上了船，那是一条虎鲨！
    你得到了 500 S币 """]

startfishingButton = InlineKeyboardButton('开始钓鱼', callback_data='fishing:fishing')
balfishingButton = InlineKeyboardButton('查看钱数💰', callback_data='fishing:bal')

kb1 = InlineKeyboardMarkup([[startfishingButton], [balfishingButton]])

def buttonCallback(update,context):
    query = update.callback_query
    print(query.data)
    if query.data == 'fishing:fishing':
        query.answer("开始钓鱼！")
        query.edit_message_text(random.choice(result30))
    if query.data == 'fishing:bal':
        query.answer("敬请等待。。。")

def fishing(update, context):
    msg = """
    欢迎来到钓鱼游戏！想知道附近的海域底下有什么吗？读读规则吧！
    1. 点击按钮来开始游戏
    2. 小心鲸鱼和鲨鱼！
    --------------------------
    玩的开心！
    """
    update.message.reply_text(msg, reply_markup=kb1)

def add_handler(dp:Dispatcher):
    fishing_handler = CommandHandler('fishing', fishing)
    dp.add_handler(CallbackQueryHandler(buttonCallback,pattern="^fishing:[A-Za-z0-9_]*"))
    dp.add_handler(fishing_handler)
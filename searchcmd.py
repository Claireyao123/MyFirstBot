from telegram.ext import Dispatcher,CommandHandler,CallbackQueryHandler
from telegram import InlineKeyboardMarkup,InlineKeyboardButton
import random
import coins

searches = [
    "有一天你决定去公园，在地上看到了一个钱包，你把它捡了起来并取走了所有的钱 (你获得了 100 S币)。一年后你被逮捕了！", 
    "有一天你决定去海底基地，由于氧气没带够而死掉了。", "有一天你决定去海底基地，不过由于没带通行证而被赶了出来。", 
    "有一天你决定去海底基地，你发现了两个稀有物种，你获得了 200 S币 作为奖励。", 
    "有一天你决定去科技馆，发现了一个传送门，你传送到了侏罗纪结果被恐龙咬死了", 
    "有一天你决定去科技馆，发现了一个传送门，你传送到了侏罗纪，你带回了一个恐龙蛋并得到了 900 S币 作为奖励！", 
    "有一天你决定去沙滩上走走，结果你被一块石头绊倒了，你花了 70 S币 治疗费", 
    "有一天你决定去医院看看，结果诈尸了，你被吓出了精神病",
    "有一天你决定去野生动物园看看，你花了 10 S币 来买门票，你看动物看的很开心", 
    "有一天你决定去潜水，结果被海浪冲跑了。当你醒来时发现你装着 1000 S币 的包不见了！哦不！以后不要潜水了！"]

startsearchButton = InlineKeyboardButton('开始搜索🔍',callback_data='search:search')
balButton = InlineKeyboardButton('查看钱数💰', callback_data='search:bal')
shopButton = InlineKeyboardButton('去商店🏠', callback_data='search:shop')

kb3 = InlineKeyboardMarkup([[startsearchButton], [balButton], [shopButton]])

def buttonCallback(update,context):
    query = update.callback_query
    if query.data == 'search:search':
        query.answer("开始搜索")
        query.edit_message_text(random.choice(searches))
    if query.data == 'search:bal': 
        query.answer("敬请等待。。。")
    
def search(update,context):
    msg="""
    欢迎来到搜索游戏，这个游戏非常冒险，确定要继续吗？如果要，请看规则：
    1. 点击按钮来开始搜索 
    2. 系统会自动找地方让你去搜索哦！
    -------------------------
    玩的开心哦！
    """
    update.message.reply_text(msg, reply_markup=kb3)
    
def add_handler(dp:Dispatcher):
    search_handler = CommandHandler('search', search)
    dp.add_handler(search_handler)
    dp.add_handler(CallbackQueryHandler(buttonCallback,pattern="^search:[A-Za-z0-9_]*"))
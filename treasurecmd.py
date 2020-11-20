from telegram.ext import Dispatcher,CommandHandler,CallbackQueryHandler
import random
from telegram import InlineKeyboardMarkup, InlineKeyboardButton

resultGM = [
    """船已经准备好了，随时出击！现在要选水手了！
    输入 /goodman 来选择好水手👨.
    输入 /badman 来选择坏水手👨.""",  
    "你本以为这次出海会一帆风顺，但现实总变质，并不是你想要的样子。就在出发前一天晚上，你的船被人偷走了！你已经没有精力来继续航行了(你失去了 20HP 和 20AP)，回家继续撸你的猫吧！"
    ]
resultBM = [
    """唉，为了省钱，你的船还是太破了，你眼睁睁的看着你的积蓄沉入了海低...
    你失去了1000XP，你已经没钱再出海了""", 
    """船虽然破，但勉强能开，
    现在来选水手吧！
    输入 /goodman 来选择好水手👨. 
    输入 /badman 来选择不好的水手👨."""]


starttreasureButton = InlineKeyboardButton('开始寻宝吧！', callback_data='treasure:treasure')
goodboatButton = InlineKeyboardButton('好船', callback_data='treasure:goodboat')
badboatButton = InlineKeyboardButton('坏船', callback_data='treasure:badboat')
goodmanButton = InlineKeyboardButton('好水手', callback_data='treasure:goodman')
badmanButton = InlineKeyboardButton('坏水手', callback_data='treasure:badman')

kb2 = InlineKeyboardMarkup([[starttreasureButton]])
kb3 = InlineKeyboardMarkup([[goodboatButton], [badboatButton]])
kb4 = InlineKeyboardMarkup([[goodmanButton], [badmanButton]])

def buttonCallback(update,context):
    query = update.callback_query
    if query.data == 'treasure:treasure':
        query.answer("开始寻宝")
        query.edit_message_text("""
        在一个风平浪静的早晨，你突然萌生了一个想法，出海寻宝！首先，你需要一搜船.
        输入 /badboat 来选择破船🚢. 
        输入 /goodboat 来选择好船🚢
        """, reply_markup=kb3)
    elif query.data == 'treasure:goodboat':
        query.answer("好船")
        query.edit_message_text(random.choice(resultGM), reply_markup=kb4)
    elif query.data == 'treasure:badboat':
        query.answer("破船")
        query.edit_message_text(random.choice(resultBM), reply_markup=kb4)
    elif query.data == 'treasure:goodman':
        query.answer("好水手")
        query.edit_message_text(random.choice(resultBM), reply_markup=kb4)
    elif query.data == 'treasure:badman':
        query.answer("坏水手")
        query.edit_message_text(random)



def treasure(update, context):
    msg1 = """
    欢迎来到寻宝游戏！这是一场惊悚又危险追逐战，智慧，运气和勇气都是成功的关键！记得要避开海盗！读一读规则吧！
    1. 系统会自动给你分配即将要发生的事，做好心理准备!
    2. 好的外表不一定有好的结果...
    3. 点击按钮开始寻宝!
    -----------------------
    请开始你的航海之旅吧！祝你玩的开心! 
    """
    update.message.reply_text(msg1, reply_markup=kb2)

def add_handler(dp:Dispatcher):
    treasure_handler = CommandHandler('treasure', treasure)
    dp.add_handler(treasure_handler)
    dp.add_handler(CallbackQueryHandler(buttonCallback,pattern="^treasure:[A-Za-z0-9_]*"))
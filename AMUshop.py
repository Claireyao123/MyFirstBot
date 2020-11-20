from telegram.ext import Dispatcher,CommandHandler,CallbackQueryHandler
from telegram import InlineKeyboardMarkup,InlineKeyboardButton
import random
import coins

crewchanceButton = InlineKeyboardButton('Crewmate Chance / 求生者机率', callback_data='power:crew')
impochanceButton = InlineKeyboardButton('Imposter Chance / 杀手机率', callback_data='power:impo')
fastButton = InlineKeyboardButton('Faster / 跑的快', callback_data='power:fast')
checkButton = InlineKeyboardButton('Check Identity / 检查身份', callback_data='power:checkI')

kb6 = InlineKeyboardMarkup([[crewchanceButton], [impochanceButton], [fastButton], [checkButton]])

def buttonCallback(update,context):
    query = update.callback_query
    if query.data == 'power:crew':
        query.answer("敬请等待。。。")

def AmongUsShop(update, context):
    update.message.reply_text("""
    Welcome to Among Us Shop! Here you can buy many power with the $AMU you win in each game!
    Crewmate Chance: 
    This can make the chance of being a crewmate larger! If you want to be a crewmate in every game, you better buy this power.
    (1000 $AMU)
    Imposter Chance: 
    This can make the chance of being a imposter larger! if you want to be an imposter in every game, you better buy this power.
    (1000 $AMU)
    Faster: 
    This can make you run faster in the game (ex. Others: speed 1.75, You: speed 2.25)
    (100 $AMU)
    Check Identity: 
    You can check if someone is imposter or not. But you can only use this one time in a game.
    (2000 $AMU)
    ______________________________________________________________________
    欢迎来到 Among Us 商店！在这里你可以用你赢得的 AMU币 买到很多特殊能力！
    求生者机率：
    这个能力可以让你成为求生者的机率更大一些
    (花费：1000 AMU币)
    杀手机率：
    这个能力可以让你成为杀手的机率更大一些
    (花费：1000 AMU币)
    跑的快：
    这个能力可以让你跑的更快(比如：别人的速度是 1.75 , 你的速度是 2.25)
    (花费：100 AMU币)
    检查身份：
    你每局可以检查一个人是不是杀手，每局只能检查一个人哦！
    (花费：2000 AMU币)
    """, reply_markup=kb6)

def add_handler(dp:Dispatcher):
    AmongUsShop_handler = CommandHandler('AmongUsShop', AmongUsShop)
    dp.add_handler(AmongUsShop_handler)
    dp.add_handler(CallbackQueryHandler(buttonCallback,pattern="^power:[A-Za-z0-9_]*"))
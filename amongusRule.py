from telegram.ext import Dispatcher,CommandHandler,CallbackQueryHandler
from telegram import InlineKeyboardMarkup,InlineKeyboardButton
import random
import AMUcoins

AMU = {}

crewmateButton = InlineKeyboardButton('Crewmate(普通人) Rules(规则)📃',callback_data='amongus:crewmate')
imposterButton = InlineKeyboardButton('Imposter(杀手) Rules(规则)📃', callback_data='amongus:imposter')
colorButton = InlineKeyboardButton('Set Color(设置颜色) 🎨', callback_data='amongus:color')
petButton = InlineKeyboardButton('Set Pet or Follower(设置随从)🐶🐱', callback_data='amongus:pet')
startButton = InlineKeyboardButton('Start Game(开始游戏) 🎮',callback_data='amongus:start' )
rewardsButton = InlineKeyboardButton('Secondly Rewards(秒福利) 💰', callback_data='amongus:rewards')

redButton = InlineKeyboardButton('红色 RED 🔴', callback_data='amongus:red')
orangeButton = InlineKeyboardButton('橙色 Orange 🟠', callback_data='amongus:orange')
yellowButton = InlineKeyboardButton('黄色 Yellow 🟡', callback_data='amongus:yellow')
greenButton = InlineKeyboardButton('绿色 Green 🟢', callback_data='amongus:green')
blueButton = InlineKeyboardButton('蓝色 Blue 🔵', callback_data='amongus:blue')
purpleButton = InlineKeyboardButton('紫色 Purple 🟣', callback_data='amongus:purple')
blackButton = InlineKeyboardButton('黑色 Black ⚫️', callback_data='amongus:black')
whiteButton = InlineKeyboardButton('白色 White ⚪️', callback_data='amongus:white')
brownButton = InlineKeyboardButton('棕色 Brown 🟤', callback_data='amongus:brown')

bedcrabButton = InlineKeyboardButton('Bedcrab 🦀️', callback_data='amongus:bedcrab')
brainslugButton = InlineKeyboardButton('Brainslug 🐌', callback_data='amongus:brainslug')
hamsterButton = InlineKeyboardButton('Hamster 🐹', callback_data='amongus:hamster')
minicButton = InlineKeyboardButton('Mini Crewmate ⛄️', callback_data='amongus:minic')
stickmanButton = InlineKeyboardButton('Stickman 🧍🏻‍♀️', callback_data='amongus:stickman')

kb3 = InlineKeyboardMarkup([[crewmateButton], [imposterButton], [colorButton], [petButton], [startButton]])
kb4 = InlineKeyboardMarkup([[redButton], [orangeButton], [yellowButton], [greenButton], [blueButton], [purpleButton], [blackButton], [whiteButton], [brownButton]])
kb5 = InlineKeyboardMarkup([[bedcrabButton], [brainslugButton], [hamsterButton], [minicButton], [stickmanButton]])

def buttonCallback(update,context):
    query = update.callback_query
    if query.data == 'amongus:crewmate':
        query.answer("请看规则👇")
        query.edit_message_text("""
        Crewmate Rules(规则)：
        1. 不要相信任何人！
        (Don't trast anyone!)
        2. 尽量独自一人活动
        (Stay just yourself, no one else)
        3. 到处走走来完成任务
        (Walking around to finish your tasks)
        4. 发现尸体后点击 Report 按钮来投票并讨论
        (Press REPORT if you found a dead body)
        5. 小心不要被杀掉！
        (Be careful! Don't be killed!)
        6. 通过点 Cafiteria 中间点 Emergency Meeting 来快速投票
        (Use the Emergency Meeting Button in Cafiteria to do a quick vote)
        -------------------
        还有什么不懂的？
        Now You Understand?
        """, reply_markup=kb3)
    if query.data == 'amongus:imposter': 
        query.answer("请看规则👇")
        query.edit_message_text("""
        Imposter Rules(规则)：
        1. 尽量使房间里只有两个人
        (Make two people stay in a room without anyone watching)
        2. 趁别人不在时杀死你旁边的人！
        (Kill the person beside you when everyone else is not here!)
        3. 假装自己无辜
        (Pretend to be a CREWMATE)
        4. 竭力辩解
        (Try to debate)
        5. 成为最后一个活着的人！
        (Be the last person alive!)
        6. 通过点 Cafiteria 中间点 Emergency Meeting 来快速投票
        (Use the Emergency Meeting Button in Cafiteria to do a quick vote)
        -------------------
        还有什么不懂的？
        Now You Undertsand?
        """, reply_markup=kb3)
    if query.data == 'amongus:color':
        query.answer("""
        选一个好看的颜色吧👇！
        Chose A Nice Color👇!
        """)
        query.edit_message_text("""
        选什么颜色好呢？
        Which Color You Want To Use In The Game?
        """, reply_markup=kb4)
    if query.data == 'amongus:red':
        query.answer("你选择了 红色 Red 🔴")
        query.edit_message_text("选择成功！Successful! 🔴", reply_markup=kb3)
    if query.data == 'amongus:orange':
        query.answer("你选择了 橙色 Orange 🟠")
        query.edit_message_text("选择成功！Successful! 🟠", reply_markup=kb3)
    if query.data == 'amongus:yellow':
        query.answer("你选择了 黄色 Yellow 🟡")
        query.edit_message_text("选择成功！Successful! 🟡", reply_markup=kb3)
    if query.data == 'amongus:green':
        query.answer("你选择了 绿色 Green 🟢")
        query.edit_message_text("选择成功！Successful! 🟢", reply_markup=kb3)
    if query.data == 'amongus:blue':
        query.answer("你选择了 蓝色 Blue 🔵")
        query.edit_message_text("选择成功！Successful! 🔵", reply_markup=kb3)
    if query.data == 'amongus:purple':
        query.answer("你选择了 紫色 Purple 🟣")
        query.edit_message_text("选择成功！Successful! 🟣", reply_markup=kb3)
    if query.data == 'amongus:black':
        query.answer("你选择了 黑色 Black ⚫️")
        query.edit_message_text("选择成功！Successful! ⚫️", reply_markup=kb3)
    if query.data == 'amongus:white':
        query.answer("你选择了 白色 White ⚪️")
        query.edit_message_text("选择成功！Successful! ⚪️", reply_markup=kb3)
    if query.data == 'amongus:brown':
        query.answer("你选择了 棕色 Brown 🟤")
        query.edit_message_text("选择成功！Successful! 🟤", reply_markup=kb3)
    if query.data == 'amongus:pet':
        query.answer('快来选一个随从吧👇！\nChose a follower！')
        query.edit_message_text("选一个吧！\nChose something！", reply_markup=kb5)
    if query.data == 'amongus:bedcrab':
        query.answer('你选择了 Bedcrab 作为你的随从！\nYou have chosed BEDCRAB to be your follower')
        query.edit_message_text("""
        Nice! You've got a follower!!!
    太好了！你有一个新的随从啦！

    Bedcrab 🦀️
        """, reply_markup=kb3)
    if query.data == 'amongus:brainslug':
        query.answer('你选择了 Brainslug 作为你的随从！\nYou have chosed BRAINSLUG to be your follower')
        query.edit_message_text("""
        Nice! You've got a follower!!!
    太好了！你有一个新的随从啦！

    Brainslug 🐌
        """, reply_markup=kb3)
    if query.data == 'amongus:hamster':
        query.answer('你选择了 Hamster 作为你的随从！\nYou have chosed HAMSTER to be your follower')
        query.edit_message_text("""
        Nice! You've got a follower!!!
    太好了！你有一个新的随从啦！

    Hamster 🐹
        """, reply_markup=kb3)
    if query.data == 'amongus:minic':
        query.answer('你选择了 Mini Crewmate 作为你的随从！\nYou have chosed MINI CREWMATE to be your follower')
        query.edit_message_text("""
        Nice! You've got a follower!!!
    太好了！你有一个新的随从啦！

    Mini Crewmate ⛄️
        """, reply_markup=kb3)
    if query.data == 'amongus:stickman':
        query.answer('你选择了 Stickman 作为你的随从！\nYou have chosed STICKMAN to be your follower')
        query.edit_message_text("""
        Nice! You've got a follower!!!
     太好了！你有一个新的随从啦！

    Stickman 🧍🏻‍♀️
        """, reply_markup=kb3)
    if query.data == 'amongus:rewards':
       query.answer("敬请等待。。。")
        
    
def AmongUs(update,context):
    msg="""
    欢迎来到 Among Us 游戏规则解说！
    1. 点击相应按钮查看不同的规则
    2. 完事儿了就可以点击开始按钮开始游戏
    --------------------------------
    玩的开心！
    ________________________________
    Welcome to Among Us !
    1. Pres different button can check different rules and set.
    2. If you are done, you can press the start button to start a game
    """
    update.message.reply_text(msg, reply_markup=kb3)
    
def add_handler(dp:Dispatcher):
    search_handler = CommandHandler('AmongUs', AmongUs)
    dp.add_handler(search_handler)
    dp.add_handler(CallbackQueryHandler(buttonCallback,pattern="^amongus:[A-Za-z0-9_]*"))
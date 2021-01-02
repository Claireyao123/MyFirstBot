from telegram.ext import Dispatcher,CommandHandler,CallbackQueryHandler
import random
from telegram import InlineKeyboardMarkup, InlineKeyboardButton

gifGOODBOAT = 'https://media3.giphy.com/media/3oz8xRQiRlaS1XwnPW/giphy.gif'
gifBADBOAT = 'https://media1.giphy.com/media/l2Je3n9VXC8z3baTe/giphy.gif'
gifGOODMAN = 'https://media4.giphy.com/media/dsKALVnvGKgn4bLu2a/giphy.gif'
gifBADMAN = 'https://media4.giphy.com/media/e37RbTLYjfc1q/giphy.gif'
gifFAST = 'https://media.tenor.com/images/e3cef91b522243efb296f3f5a9b750a6/tenor.gif'
gifSLOW = 'https://media4.giphy.com/media/5qVezULI35guQ/200.gif'
gifYW = 'https://i.imgur.com/L32gUzm.gif'
gifNW = 'https://media1.giphy.com/media/JRbW288WAWvECVyYwx/giphy.gif'
gifFIGHT = 'https://www.spiritshunters.com/wp-content/uploads/2018/09/KRAKEN_v2.gif'
gifRUN = 'https://media3.giphy.com/media/IdTBkruzkGeq1HEnlP/source.gif'
gifDRINK = 'https://media4.giphy.com/media/5zjdD5R7crDK37nqTX/giphy-downsized-medium.gif'
gifDANCE = 'https://media2.giphy.com/media/cm6bHfo16WBokQuFqa/giphy.gif'
gifEARLY = 'https://i.pinimg.com/originals/c6/fb/94/c6fb94ee41fb968e27ad009047f0a4cb.gif'
gifLATE = 'https://media3.giphy.com/media/U2S7MdmsC0O5WDReuE/giphy.gif'
gifFACE = 'https://i.gifer.com/9pd0.gif'
gifAWAY = 'https://media0.giphy.com/media/l0Hedc94pmNdUA2Ji/source.gif'
gifCHECK = 'https://media4.giphy.com/media/3owzW5c1tPq63MPmWk/giphy.gif'
gifHAPPY = 'https://media0.giphy.com/media/3o6Mbl0kpk4i9G2GCQ/source.gif'
gifYEW = 'https://media3.giphy.com/media/3o6Ztn4vuACOmS0Mla/source.gif'
gifNOW = 'https://media1.giphy.com/media/4EF5LwiRfpBKQUOsoF/giphy.gif'
gifISLAND = 'https://thumbs.gfycat.com/SmallIncredibleAttwatersprairiechicken-small.gif'
gifSHIP = 'https://media0.giphy.com/media/3og0ILtBPzSsVnrTry/source.gif'


starttreasureButton = InlineKeyboardButton('开始寻宝吧！', callback_data='treasure:treasure')
goodboatButton = InlineKeyboardButton('好船', callback_data='treasure:goodboat')
badboatButton = InlineKeyboardButton('坏船', callback_data='treasure:badboat')
goodmanButton = InlineKeyboardButton('好水手', callback_data='treasure:goodman')
badmanButton = InlineKeyboardButton('坏水手', callback_data='treasure:badman')
fastButton = InlineKeyboardButton('快一点', callback_data='treasure:fast')
slowButton = InlineKeyboardButton('慢一点', callback_data='treasure:slow')
ywButton = InlineKeyboardButton('去散步', callback_data='treasure:yw')
nwButton = InlineKeyboardButton('不去散步', callback_data='treasure:nw')
fightButton = InlineKeyboardButton('战斗', callback_data='treasure:fight')
runButton = InlineKeyboardButton('逃跑', callback_data='treasure:run')
drinkButton = InlineKeyboardButton('喝酒',callback_data='treasure:drink')
danceButton = InlineKeyboardButton('跳舞',callback_data='treasure:dance')
earlyButton = InlineKeyboardButton('早起',callback_data='treasure:early')
lateButton = InlineKeyboardButton('晚起',callback_data='treasure:late')
awayButton = InlineKeyboardButton('绕开',callback_data='treasure:away')
faceButton = InlineKeyboardButton('迎战',callback_data='treasure:face')
happyButton = InlineKeyboardButton('狂欢',callback_data='treasure:happy')
checkButton = InlineKeyboardButton('查看方位',callback_data='treasure:check')
yewButton = InlineKeyboardButton('放哨',callback_data='treasure:yew')
nowButton = InlineKeyboardButton('不要放哨',callback_data='treasure:now')
islandButton = InlineKeyboardButton('岛上过夜',callback_data='treasure:island')
shipButton = InlineKeyboardButton('回船过夜',callback_data='treasure:ship')


kb2 = InlineKeyboardMarkup([[starttreasureButton]])
kb3 = InlineKeyboardMarkup([[goodboatButton], [badboatButton]])
kb4 = InlineKeyboardMarkup([[goodmanButton], [badmanButton]])
kb5 = InlineKeyboardMarkup([[fastButton], [slowButton]])
kb6 = InlineKeyboardMarkup([[ywButton],[nwButton]])
kb7 = InlineKeyboardMarkup([[fightButton],[runButton]])
kb8 = InlineKeyboardMarkup([[drinkButton],[danceButton]])
kb9 = InlineKeyboardMarkup([[earlyButton],[lateButton]])
kb10 = InlineKeyboardMarkup([[awayButton],[faceButton]])
kb11 = InlineKeyboardMarkup([[happyButton],[checkButton]])
kb12 = InlineKeyboardMarkup([[yewButton],[nowButton]])
kb13 = InlineKeyboardMarkup([[islandButton],[shipButton]])


def buttonCallback(update,context):
    query = update.callback_query
    if query.data == 'treasure:treasure':
        query.answer("开始寻宝")
        query.edit_message_text("""
        在一个风平浪静的早晨，你突然萌生了一个想法，出海寻宝！首先，你需要一搜船.选哪艘船好呢？
        """, reply_markup=kb3)
    elif query.data == 'treasure:goodboat':
        query.answer("好船")
        query.edit_message_animation(gifGOODBOAT,caption='船已经准备好了！现在选好水手还是坏水手？',reply_markup=kb4)
    elif query.data == 'treasure:badboat':
        query.answer("破船")
        query.edit_message_animation(gifBADBOAT,caption='为了省钱，你的船还是太破了。。。你眼睁睁的看着你的积蓄沉入海底，还是回家撸猫吧。。')
    elif query.data == 'treasure:goodman':
        query.answer("好水手")
        query.edit_message_animation(gifGOODMAN,caption='大家和乐融融就像是一家人，接下来选择一个速度吧！',reply_markup=kb5)
    elif query.data == 'treasure:badman':
        query.answer("坏水手")
        query.edit_message_animation(gifBADMAN,caption='你的船员发生了暴动，他们把你扔下了海并开船逃走了。')
    elif query.data == 'treasure:fast':
        query.answer("快一点")
        query.edit_message_animation(gifFAST,caption='你的船开的太快了！彻底散架了！')
    elif query.data == 'treasure:slow':
        query.answer("慢一点")
        query.edit_message_animation(gifSLOW,caption='船员都好兴奋！你想带你都船员们去甲板上散步吗？',reply_markup=kb6)
    elif query.data == 'treasure:yw':
        query.answer("去散步")
        query.edit_message_animation(gifYW,caption='海风吹过面颊，兴奋的船员们安静了下来。哦不！你们遇到了巨乌贼海怪克拉肯！战斗还是逃跑？',reply_markup=kb7)
    elif query.data == 'treasure:nw':
        query.answer("不去散步")
        query.edit_message_animation(gifNW,caption='你的船员都呆在船舱里喝酒而没有看到海怪克拉肯，所有人都被吃掉了！')
    elif query.data == 'treasure:fight':
        query.answer("战斗")
        query.edit_message_animation(gifFIGHT,caption='不愧是久经沙场的老水手，大家齐心协力的把海怪打跑了！接下来做什么呢？',reply_markup=kb8)
    elif query.data == "treasure:run":
        query.answer("逃跑")
        query.edit_message_animation(gifRUN,caption='只见海怪用力一劈，整艘船断成了两截，所有人直接归西...')
    elif query.data == 'treasure:drink':
        query.answer("喝酒")
        query.edit_message_animation(gifDRINK,caption='所有人喝的烂醉如泥。明天是早起还是晚起呢？',reply_markup=kb9)
    elif query.data == 'treasure:dance':
        query.answer("跳舞")
        query.edit_message_animation(gifDANCE,caption='大家载歌载舞，别提多开心了！明天是早起还是晚起呢？',reply_markup=kb9)
    elif query.data == 'treasure:early':
        query.asnwer("早起")
        query.edit_message_animation(gifEARLY,caption='船员们因为休息太少而无精打采，懒洋洋的。仔细一看，远处有个小黑点，哦不！那是海盗船！幸好他们还没发现你们！现在要绕开还是战斗？',reply_markup=kb10)
    elif query.data == 'treasure:late':
        query.answer("晚起")
        query.edit_message_animation(gifLATE,caption='哦不！你们睡觉的时候海盗偷偷登船并杀死了所有人并带着所有的东西溜之大吉了！')
    elif query.data == 'treasure:away':
        query.answer("绕开")
        query.edit_message_animation(gifAWAY,caption='海盗才不吃你这一套，用大炮把你的船打沉了！')
    elif query.data == 'treasure:face':
        query.answer("迎战")
        query.edit_message_animation(gifFACE,caption='战斗的号角已吹响，你在最前面猛砍猛杀，船员们气势高涨！海盗们还是逃走了几个，不过你也没多想！你犯了一个致命的错误...接下来怎么办？',reply_markup=kb11)
    elif query.data == 'treasuer:happy':
        query.answer("狂欢")
        query.edit_message_animation(gifHAPPY,caption='所有人尽情狂欢，船漂到了百慕大三角，所有人葬身海底')
    elif query.data == 'treasure:check':
        query.answer("查看方位")
        query.edit_message_animation(gifCHECK,capyion='你们发现自己离小岛不远了！需要有人放哨吗？',reply_markup=kb12)
    elif query.data == 'treasure:yew':
        query.answer("放哨")
        query.edit_message_animation(gifYEW,caption='幸亏有人放哨，你们及时发现了海盗，把海盗打跑了以后你们取出了埋在沙子里的宝箱！现在要在岛上过夜还是回船？',reply_markup=kb13)
    elif query.data == 'treasure:now':
        query.answer("不要放哨")
        query.edit_message_animation(gifNOW,caption='逃跑的海盗冲出来把所有人都绑架了！')
    elif query.data == 'treasure:island':
        query.answer("岛上过夜")
        query.edit_message_animation(gifISLAND,caption='你和你的船员们一起在岛上的树林里露宿去了，结果被岛上的野人发现并杀死了！')
    elif query.data == 'treasure:ship':
        query.answer("回船过夜")
        query.edit_message_animation(gifSHIP,caption='你和你的船员们把财宝带上了船并回到了港口！你成功了！现在你是独一无二的优秀船长！太厉害啦！！！这 15000XP 50AP 200GP 是从宝箱里取出来的奖励！好好使用它吧！寻宝游戏圆满结束啦！使用 /start 来看看玩点别的什么吧！')
    
    




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
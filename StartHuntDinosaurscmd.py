from telegram.ext import Dispatcher,CommandHandler
import random
result15 = ["你背上猎枪决定去猎恐龙。你潜伏在了草丛里，一个黑影闪过，你纵身一跃并逮住了它！\n你捕获到了一只 似鸟龙 ！\n(你得到了 10XP !)", "你背上猎枪决定去猎恐龙。你潜伏在了草丛里，一个黑影闪过，你纵身一跃并逮住了它！你捕获了一只 小弯龙 !\n(你得到了 15XP !)", "你背上猎枪决定去猎恐龙。你潜伏在了草丛里，一个黑影闪过，你纵身一跃并逮住了它！你捕获了一只 三角龙 !\n(你得到了 50XP !)", "你饿这肚子回到了属于你的时代，一只恐龙都没捕到 T_T \n(你失去了 10AP )", "你拼尽全力扑向了 特暴龙 , 结果对方一下就把你甩开了\n(你失去了 20HP )", "你看到了对面洞穴里有东西，于是前去查看，竟然是 鸭嘴龙 的蛋！(你得到了 200XP )", "你背上猎枪决定去猎恐龙。你潜伏在了草丛里，一个黑影闪过，你纵身一跃并逮住了它！你捕获了一只 包龙 !\n(你得到了 30XP )", "你背上猎枪决定去猎恐龙。你潜伏在了草丛里，一个黑影闪过，你纵身一跃并逮住了它！你竟然捕获到了一只 霸王龙 ! 连你自己都不相信你的运气！\n(你得到了 600XP )", "你走着走着突然看到了一个恐龙猎人的包，里面有一些药和钱! \n(你得到了 10GP 并恢复了 5HP )"]

def StartHuntDinosaurs(update, context):
    update.message.reply_text(random.choice(result15))

def add_handler(dp:Dispatcher):
    StartHuntDinosaurs_handler = CommandHandler('StartHuntDinosaurs', StartHuntDinosaurs)
    dp.add_handler(StartHuntDinosaurs_handler)
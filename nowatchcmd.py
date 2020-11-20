from telegram.ext import Dispatcher,CommandHandler
import random

def nowatch(update, context):
    update.message.reply_text("你们光顾着挖宝藏了，没有发现海盗们躲在暗处。突然你的脖子上挨了一刀，美丽的世界与你分别了！\n还是要恭喜你，你克服了前面的重重考验，不过你栽在了这最后一关上！这 5000XP 是你赢得的奖励！")

def add_handler(dp:Dispatcher):
    nowatch_handler = CommandHandler('nowatch', nowatch)
    dp.add_handler(nowatch_handler)
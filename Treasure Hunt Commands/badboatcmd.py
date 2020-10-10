from telegram.ext import Dispatcher,CommandHandler
import random
result = ["唉，为了省钱，你的船还是太破了，你眼睁睁的看着你的积蓄沉入了海低...\n你失去了1000XP，你已经没钱再出海了", "船虽然破，但勉强能开，现在来选水手吧！\n输入 /goodman 来选择好水手👨. \n输入 /badman 来选择不好的水手👨."]

def badboat(update, context):
 update.message.reply_text(random.choice(result))

def add_handler(dp:Dispatcher):
    badboat_handler = CommandHandler('badboat', badboat)
    dp.add_handler(badboat_handler)
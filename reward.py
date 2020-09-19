import random
from telegram.ext import CommandHandler
def reward(update, context):
    reward = ["你得到了90XP, 还不错哦! \nYou got 90XP which was good enough! ", "你得到了40XP, 貌似有点少... \nYou got 40XP, seems a little bit little...", "哈哈，啥都没有！\nHa Ha! Nothing!", "运气也太好了吧？200XP? \nYou are so lucky? 200XP?", "100XP, 嫌少吗？\n100XP, less?"]
    context.bot.send_message(chat_id=update.effective_chat.id, text=random.choice(reward))

def add_dispatcher(dispatcher):
    reward_handler = CommandHandler('reward', reward)
    dispatcher.add_handler(reward_handler)
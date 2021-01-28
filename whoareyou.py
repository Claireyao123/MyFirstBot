from telegram.ext import Dispatcher,CommandHandler,CallbackQueryHandler
from telegram import InlineKeyboardMarkup,InlineKeyboardButton, BotCommand
import random

def whoAreYou(update,context):
    msg = [
        """You can call me Operation Lune 9000, I'm actually just a random reply AI(not really)""",
        """Bro, I'm Operation Lune 9000, I am an emotional AI with supercalifregeristicexpialidocious brain!""",
        """I'm gonna be your first personal AI, you can call me Operation Lune 9000!""",
        """I am a random Sentence AI Operation Lune 9000, you can ask me anything!""",

    ]
    update.message.reply_text("Hey, it seems that you are understanding who I am, let me tell you more :D \n%s"%(random.choice(msg)))

def add_handler(dp:Dispatcher):
    About_handler = CommandHandler('About', whoAreYou)
    dp.add_handler(About_handler)
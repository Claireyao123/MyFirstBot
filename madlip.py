from telegram.ext import Dispatcher,CommandHandler
import random

story = [
   ""
]

def randomStory(update, context):
    update.message.reply_text(random.choice(msg))

def add_handler(dp:Dispatcher):
    story_handler = CommandHandler('madlib', randomStory)
    dp.add_handler(story_handler)
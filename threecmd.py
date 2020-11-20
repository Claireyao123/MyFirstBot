from telegram.ext import Dispatcher,CommandHandler
import random

def three(update, context):
    update.message.reply_text("你准备的船太少了，船员们以为你很偏爱，所以找了个月黑风高的夜晚把你扔进了水了...一群愚民啊！！！")

def add_handler(dp:Dispatcher):
    three_handler = CommandHandler('three', three)
    dp.add_handler(three_handler)
from telegram.ext import Dispatcher,CommandHandler
import random

def CanadaHistoryChinese(update, context):
    update.message.reply_text("很高兴你能按时完成你的作业，点击这个链接来查看加拿大历史简介吧！⬇️\nhttps://baike.baidu.com/item/%E5%8A%A0%E6%8B%BF%E5%A4%A7%E5%8E%86%E5%8F%B2/7638777")

def add_handler(dp:Dispatcher):
    CanadaHistoryChinese_handler = CommandHandler('CanadaHistoryChinese', CanadaHistoryChinese)
    dp.add_handler(CanadaHistoryChinese_handler)
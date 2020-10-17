from telegram.ext import Dispatcher,CommandHandler
import random

def ChinaHistoryChinese(update, context):
    update.message.reply_text("很高兴你能按时完成你的作业，点击这个链接来查看中国历史简介吧⬇️！\nhttps://baike.baidu.com/item/%E4%B8%AD%E5%9B%BD%E5%8E%86%E5%8F%B2/152769")

def add_handler(dp:Dispatcher):
    ChinaHistoryChinese_handler = CommandHandler('ChinaHistoryChinese', ChinaHistoryChinese)
    dp.add_handler(ChinaHistoryChinese_handler)
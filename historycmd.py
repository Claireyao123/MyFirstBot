from telegram.ext import Dispatcher,CommandHandler
import random

def history(update, context):
    update.message.reply_text("欢迎来到历史作业辅导！准备开始窜改历史了吗？看看规则吧！\n1. 此程序为历史考试与历史作业而设计，不是让你们玩的啊！\n2. 看看选项吧！\n输入 /CanadaHistoryChinese 来查看加拿大历史简介(中文版)\n输入 /ChinaHistoryChinese 来查看中国历史简介(中文版) \n------------------------\n祝你们做 历史作业/历史考试 开心")

def add_handler(dp:Dispatcher):
    history_handler = CommandHandler('history', history)
    dp.add_handler(history_handler)
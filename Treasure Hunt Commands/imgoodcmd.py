from telegram.ext import Dispatcher,CommandHandler
import random

def imgood(update, context):
    update.message.reply_text("只见SCP-049放松了下来，并同意继续接受采访。\n不愧是你！你成功的让SCP-049安静了下来！\n解说：\n如果SCP-049感觉周围有他所称的“瘟疫”存在，他就会询问那个人感觉是否良好。如果那个人拒绝，SCP-049就会杀死那人。\n你帮助了基金会收容了SCP-049，所以基金会决定送你 700XP 作为奖励！\n回到 /start 看看玩点别的什么吧！")

def add_handler(dp:Dispatcher):
    imgood_handler = CommandHandler('imgood', imgood)
    dp.add_handler(imgood_handler)
import config
from telegram import Update,Animation,PhotoSize,Audio,Sticker,Document,Voice,Video,VideoNote
from telegram.ext import Dispatcher,CommandHandler,CallbackContext
from json import dumps


def info(update:Update,context:CallbackContext):
    u = str(update)
    u = dumps(eval(u))
    # msgType = update.message.
    # msg = "This is a %s\n===================\n%s"%(,u)
    # context.bot.send_message(chat_id=update.effective_chat.id,text=msg)
    #  https://python-telegram-bot.readthedocs.io/en/stable/telegram.message.html#telegram.Message
    msg = ""
    if update.message.reply_to_message.video:
        msg = 'That\'s a video'
    elif update.message.reply_to_message.voice:
        msg = 'That\'s a voice'
    elif update.message.reply_to_message.animation:
        msg = 'That\'s an animation'
    elif update.message.reply_to_message.video_note:
        msg = 'That\'s a video note'
    elif update.message.reply_to_message.document:
        msg = 'That\'s a document'
    elif update.message.reply_to_message.sticker:
        msg = 'That\'s a sticker'
    elif update.message.reply_to_message.audio:
        msg = 'That\'s an audio'
    elif update.message.reply_to_message.message:
        msg = 'That\'s a message'

    update.message.reply_text(msg,u)

def add_dispatcher(dp: Dispatcher):
    dp.add_handler(CommandHandler(["info"], info))
    return []
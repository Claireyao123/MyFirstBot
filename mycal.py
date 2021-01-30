from icalevents.icalevents import events
from datetime import date, timedelta
from telegram.ext import CallbackContext, Dispatcher, CommandHandler
from telegram import Update
import pytz
import config

cals = config.CONFIG["cals"]
print(f"cals:{cals}")

def save():
    config.CONFIG["cals"] = cals
    config.save_config()

def timer_callback(update, context: CallbackContext):
    if len(context.args) == 3:
        chat = context.args[0]
        time = context.args[1]
        urls = context.args[2]
    save()
    tomorrow = date.today() + timedelta(days=1)
    msg = ""
    es = events(urls,fix_apple=True, start=tomorrow, end=tomorrow)
    for e in es:
        msg += f"{e.summary} start:{e.start} end:{e.end} {e.description}"
    context.bot.send_message(chat_id=chat,text=msg)

def cal(update,context):
     if len(context.args) == 3:
        chat = context.args[0]
        time = context.args[1]
        urls = context.args[2]
    save()
    context.job_queue.run_repeating(timer_callback,time,context=chat)

def run_repeating(update,context,job_queue):
         if len(context.args) == 3:
        chat = context.args[0]
        time = context.args[1]
        urls = context.args[2]
    save()
    j = job_queue.run_daily(timer_callback,timedelta(hour=11,minute=50,tzinfo=pytz.timezone('US/Eastern')), context=chat)
    update.effective_message.reply_text(f"From now on, I will be starting to send message to you every hour.")

def add_handler(dp:Dispatcher):
    cal_handler = CommandHandler('set_cal', cal)
    dp.add_handler(cal_handler)
    dp.add_handler(c_handler)
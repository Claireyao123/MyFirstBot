from icalevents.icalevents import events
from datetime import date, timedelta
from telegram.ext import CallbackContext, Dispatcher, CommandHandler
from telegram import Update
import pytz

def timer_callback(context: CallbackContext):
    tomorrow = date.today() + timedelta(days=1)
    msg = ""
    url = "webcal://p60-caldav.icloud.com/published/2/MTMwMjQzNDk4NDEzMDI0M3sQtDCMMqfWL7VMca-urO1PHNC7k1S3xOJlT4pbFvB2zTOKsoMYKAaoX8kwofUBGi0yjak_7FqpXGZUZh5MhGY"
    es = events(url,fix_apple=True, start=tomorrow, end=tomorrow)
    for e in es:
        msg += f"{e.summary} start:{e.start} end:{e.end} {e.description}"
    context.bot.send_message(chat_id=context.job.context,text=msg)

def cal(update,context):
    chatid = update.effective_chat.id
    context.job_queue.run_repeating(timer_callback,5,context=chatid)

def run_repeating(update,job_queue):
    chat_id = update.effective_chat.id
    j = job_queue.run_daily(timer_callback,timedelta(hour=11,minute=50,tzinfo=pytz.timezone('US/Eastern')), context=chat_id)
    update.effective_message.reply_text(f"Start sending message, next time:(j.next)")

def add_handler(dp:Dispatcher):
    cal_handler = CommandHandler('MyCal', cal)
    dp.add_handler(cal_handler)
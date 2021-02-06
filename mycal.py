import pytz
from icalevents.icalevents import events
from datetime import datetime, timedelta, date, time
from telegram.ext import JobQueue, CommandHandler, Updater
from telegram import bot
import config


cals = config.CONFIG['cal']

def save():
    config.CONFIG['cal'] = cals
    config.save_config()    

def get_cal(context):
    job = context.job
    t = date.today()
    tmr = t + timedelta(days=1)
    es = events(url=cals[str(job.context)]['url'],start=tmr,end=tmr,fix_apple=True)
    msg = "Tomorrow's calendar:"
    if len(es) == 0:
        msg = 'Yey! Nothing for tomorrow!'
    for thing in es:
        description = str(thing.description)
        if description == 'None':
            description = 'No description'
        msg += f'''
========================
{thing.summary}: {description}
    Starts: {datetime.strftime(thing.start,"%Y/%m/%d %H:%M:%S")}
    Ends: {datetime.strftime(thing.end,"%Y/%m/%d %H:%M:%S")}'''
    context.bot.send_message(job.context,msg)

def show_cal(update,context):
    msg = 'Here is your calendar:'
    for chatid in cals:
        msg += f'''
========================
📆 {chatid}:
    Calendar: {cals[chatid]['url']}
    Time: {cals[chatid]['time'][0]}:{cals[chatid]['time'][1]}
    Timezone: {cals[chatid]['time'][2]}'''
    update.message.reply_text(msg)

def show_job(update,context):
    msg = 'Here is what you should do:'
    for job in context.job_queue.jobs():
        msg += f'\n{job.name}: {datetime.strftime(job.next_t,"%H:%M")}'
    update.message.reply_text(msg)

def set_cal(update,context):
    uid = update.effective_user.id
    if not uid in config.CONFIG['admin']:
        update.message.reply_text('OMG, you are not in an admin!')
        return
    if len(context.args) == 0:
        update.message.reply_text('Pls don\'t act stupid and pls use this format:\n/get_cal@ClaireSuperBot "Calendar URL. ex.Nothing" "The Time You Want To Get Nonfictions. ex. 19:00" "Your Timezone. ex.US/Eastern" Research some of the timezone online pls.')
        return
    if len(context.args) > 3:
        update.message.reply_text('WTH are you saying?')
        return
    url = context.args[0]
    time = context.args[1]
    timezone = context.args[2]
    chatid = update.effective_chat.id
    if not timezone in pytz.all_timezones:
        update.message.reply_text('Ah oh! This is not a valide time-zone.')
        return
    cals[str(chatid)] = {}
    cals[str(chatid)]['url'] = url
    strhours,strminutes = time.split(':')
    hours = int(strhours)
    minutes = int(strminutes)
    if hours > 23 or hours < 0:
        update.message.reply_text("OMG Don\'t be someone who is stupid, do you know that a day has twenty-four hours? Pls go back to grade one and start your school year all again!")
        return
    if minutes >= 60 or minutes < 0:
        update.message.reply_text("Don\'t be someone who is stupid, do you know that a hour has sixty minutes? If not, you really should go back to grade one and start your school year all again!")
        return
    cals[str(chatid)]['time'] = [hours,minutes,timezone]
    update.message.reply_text(f'Oh yey! You can get nonfictions every day at {time}!')
    run_daily(context.job_queue)

def run_daily(job_queue):
    for chatid in cals:
        calstuff = cals[chatid]
        for job in job_queue.jobs():
            if job.name == chatid:
                job.schedule_removal()
        job_queue.run_daily(get_cal,time(calstuff['time'][0],calstuff['time'][1],0,0,pytz.timezone(calstuff['time'][2])),context=chatid,name=chatid)

def add_handler(dp):
    dp.add_handler(CommandHandler('set_cal',set_cal))
    dp.add_handler(CommandHandler('show_cal',show_cal))
    dp.add_handler(CommandHandler('show_jobs',show_job))
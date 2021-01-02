from datetime import datetime,timedelta
from telegram.ext import Dispatcher,CommandHandler,Filters
from telegram import BotCommand
import config 
import random

def gif(update,context):
    gifs = ['https://www.estiponagroup.com/sites/default/files/fishing.gif','https://www.pbh2.com/wordpress/wp-content/uploads/2014/09/This-Jump-For-Fun.gif','https://crazyhyena.com/imagebank/g/crazy-gif-falling-through-ice-into-lake.gif','https://media1.tenor.com/images/f89d22401cc2f5fa021b6b87ff13e12a/tenor.gif','https://gifrific.com/wp-content/uploads/2014/02/Ice-Break-Fail-and-Fall-Into-Water.gif','https://i.imgur.com/IgOSBAt.gif','https://media1.tenor.com/images/bf55749ae0b93b56f2044f563b3c9fbb/tenor.gif','https://www.pbh2.com/wordpress/wp-content/uploads/2013/11/falling-into-a-lake.gif','https://media1.tenor.com/images/719afb36ecc6a0530c96391a52a0e705/tenor.gif']
    gif = random.choice(gifs)
    update.message.reply_animation(gif,caption="hi")

def add_handler(dp:Dispatcher):
    gif_handler = CommandHandler('GIF', gif)
    dp.add_handler(gif_handler)

def get_command():
    return [BotCommand('gif',gif)]
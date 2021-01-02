from telegram.ext import Dispatcher,CommandHandler,CallbackQueryHandler
import random
from telegram import InlineKeyboardMarkup, InlineKeyboardButton

whyButton = InlineKeyboardButton('Why Zebra Mussels are dangerous?', callback_data='danger:why')
whatButton = InlineKeyboardButton('Who they affect the most?', callback_data='danger:who')
humanButton = InlineKeyboardButton('Does they affect humans?', callback_data='danger:human')
howButton = InlineKeyboardButton('How they travel and invase?', callback_data='danger:how')

kb109 = InlineKeyboardMarkup([[whyButton], [whatButton], [humanButton], [howButton]])

def buttonCallback(update,context):
    query = update.callback_query
    if query.data == 'danger:why':
        query.edit_message_text("""
        Zebra Mussels are very dangerous because they can affect the food chain where they live. Zebra Mussels usually kill down a lot of animals which are very important for the food chain adn the ecosystem. They also cause a lot of damages to our ships and boats, they will destroy the engine and cause some danger and a lot of money.
        """)
    elif query.data == 'danger:who':
        query.edit_message_text("Zebra Mussels mostly effect the planktons and fish eggs in the area, but sometimes they will also affect the ships and destroy the engine.")
    elif query.data == 'danger:human':
        query.edit_message_text("Zebra Mussels cause some damages to humans because they can destroy the ship, and they might cause some danger to people who are on the ship.")
    elif query.data == 'danger:how':
        query.edit_message_text("Zebra Mussels travel on the bottom of the ships and boats. They can travel to everywhere and they will brake the ships.")


def Dangerous(update,context):
    msg109 = ("""
    Hi! It's me again :) So happy that you use our robot QvQ Press different button to read different informations! 
    --------------
    Of course there will be some questions that you will want to ask, so send my an email if you need!
    ______________________________
    """)
    update.message.reply_text(msg109, reply_markup=kb109)

def add_handler(dp:Dispatcher):
    Dangerous_handler = CommandHandler('Dangerous', Dangerous)
    dp.add_handler(Dangerous_handler)
    dp.add_handler(CallbackQueryHandler(buttonCallback,pattern="^danger:[A-Za-z0-9_]*"))
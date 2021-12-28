from telegram import Update
from telegram.ext import Updater , CommandHandler, CallbackQueryHandler, CallbackContext,Filters,MessageHandler
import os

Token =os.environ.get("BOT_TOKEN",None)
updater = Updater( Token ,use_context = True )

def start(updater,context):
 updater.message.reply_text('''
 
 Hello! 👋

Welcome to the VIP community.

This is basic info about a form of Signal you need to know

- Target/ Entry/ SL are clear in  Signal.
- Trade is opened at Entry
- Trade is closed at TP
- Trade is closed at Stop loss

- If there is no update, just follow info given at original signal

- If there is new update something like ( cancel trade, or take profit partially ...etc), follow new update posts.

- When price is moving on right way, It is recommended to move stoploss price to profit zone.

- When price come to 1st Target zone, It is better to take profit one part. let the rest run to profit.

‼ You need to know that you need to spend a maximum of 5% of your money on each signal.
 
 Use the limit order option on the coin what you want to trade and change the limit buy price for every order.

Example: 

When you want to buy bitcoin for 100 dollars in total you can ladder it between 40 and 42K.

42.0K – Limit buy $20
41.5K – Limit buy $20
41.0K – Limit buy $20
40.5K – Limit buy $20
40.0K – Limit buy $20

Total: $100

The average price you bought now is 41.0K instead of 42.0K when you bought all 100 dollars at 42.0K

Benefits:
- You have a lower average buy so you have faster and more profits when Bitcoin drops to 40K and then go up again to for example 50K. You also have less loss when Bitcoins dumps to 39K for example.

Downside:
- When bitcoin only dips to 41K, it hits only 50% of your buys. So, you have little Bitcoin to gain profits BUT you didn’t lose money!

This is basically how to trade on the calls in the channel

TIP: set your limit order always at 41.020 for example instead of 41.000 to get a higher chance of hitting your buys.

For laddered selling it comes down to the same thing.
 

  ''')
 
 
 
 
def help(updater,context):
 updater.message.reply_text("Add me to your group ")
 

def add_group(update: Update, context: CallbackContext):
    for member in update.message.new_chat_members:
        update.message.reply_text(f'Hello {member.full_name} , Welcome to ln support Thank you for Joining  ')

add_group_handle = MessageHandler(Filters.status_update.new_chat_members, add_group)
updater.dispatcher.add_handler(add_group_handle)

dp =updater.dispatcher.add_handler
dp(CommandHandler('start',start))
dp(CommandHandler('help',help))

updater.start_polling()
updater.idle()

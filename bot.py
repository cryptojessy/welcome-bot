from telegram import Update
from telegram.ext import Updater , CommandHandler, CallbackQueryHandler, CallbackContext,Filters,MessageHandler
import os

Token =os.environ.get("BOT_TOKEN",None)
updater = Updater( Token ,use_context = True )

def start(updater,context):
 updater.message.reply_text('''
 
 Hello, "member.full_name"! 👋 "first_name"! 👋

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

You need to know that you need to spend a maximum of 5% of your money on each signal.
 
 
 
 
 
 
 Hi iam welcome messanger bot 
Add me to your group  testvame tuka gluposti
 
 Made with Love ❤️ by @lntechnical

  ''')
 
 
 def start(updater,context):
 updater.message.reply_text('''
 vtoro saobshtenie
 
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

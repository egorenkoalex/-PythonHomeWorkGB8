from telegram import Update
from telegram.ext import Updater, ApplicationBuilder, CommandHandler, CallbackContext
import datetime



def log(update: Update, contex: CallbackContext):
    with open('db.csv', 'a') as file:
        file.write(f'{update.effective_user.first_name},{update.effective_user.id},\
            {update.message.text}, {datetime.datetime.now().time()}\n')
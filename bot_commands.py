from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
import calcul
import spy

async def hi(update: Update, context: ContextTypes.DEFAULT_TYPE):
    spy.log(update, context)
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    spy.log(update, context)
    await update.message.reply_text(f'/hi\n/time\n/help\n/calc')

async def time(update: Update, context: ContextTypes.DEFAULT_TYPE):
    spy.log(update, context)
    await update.message.reply_text(f' {datetime.datetime.now().time()}')

async def calc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    spy.log(update, context)
    msg = update.message.text
    exp = msg.split(' ')
    num1 = exp[1]
    op = exp[2]
    num2 = exp[3]
    a=num1
    b=num2
    c=op
    result = calcul.tudy(num1, num2, op)
    print(result)
    await update.message.reply_text(f'{result}')
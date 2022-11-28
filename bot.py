
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import * 



app = ApplicationBuilder().token("5751750441:AAHzJdMGka7IRjEE0hRvt-hnnNo8KWGn24k").build()

app.add_handler(CommandHandler("hi", hi))
app.add_handler(CommandHandler("help", help))
app.add_handler(CommandHandler("time", time))
app.add_handler(CommandHandler("calc", calc))
#app.add_handler(CommandHandler("hello", hello))

print('server start')
app.run_polling()
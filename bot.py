from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *
import os

# os.getenv('token_tg')
app = ApplicationBuilder().token("5433122929:AAEeUN3olLSvE4iDwZDNJUNiVvtdG4ipfd4").build()

app.add_handler(CommandHandler("hello", hello_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("sum", sum_command))
app.add_handler(CommandHandler("diff", diff_command))
app.add_handler(CommandHandler("mult", mult_command))
app.add_handler(CommandHandler("div", div_command))
print("it's OK!")

app.run_polling()

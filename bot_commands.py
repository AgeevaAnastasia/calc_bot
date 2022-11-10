from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
from fractions import Fraction


async def hello_command(update: Update, context: ContextTypes.context):
    await update.message.reply_text(f'Hello, {update.effective_user.first_name}!')


async def help_command(update: Update, context: ContextTypes.context):
    await update.message.reply_text(f'/hello \n/time \n/help \n/sum число1 число2 \n/diff число1 число2 \n/mult число1 число2 \n/div число1 число2')


async def time_command(update: Update, context: ContextTypes.context):
    await update.message.reply_text(f'Сейчас {datetime.datetime.now().time()}')


async def sum_command(update: Update, context: ContextTypes.context):
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} + {y} = {x + y}')


async def diff_command(update: Update, context: ContextTypes.context):
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} - {y} = {x - y}')


async def mult_command(update: Update, context: ContextTypes.context):
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} * {y} = {x * y}')


async def div_command(update: Update, context: ContextTypes.context):
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    if y != 0:
        await update.message.reply_text(f'{x} / {y} = {x / y}')
    else:
        await update.message.reply_text(f'на ноль не делим :)')

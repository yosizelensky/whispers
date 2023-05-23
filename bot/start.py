# encoding: utf-8

from logging import getLogger

from telegram import Update
from telegram.ext import CallbackContext, CommandHandler, Dispatcher

# Init logger
logger = getLogger(__name__)

from telegram.ext import CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
############################### Bot ############################################
def start(update, context):
  update.message.reply_text(menu_message(),
                            reply_markup=main_menu_keyboard())

def main_menu(update,context):
  query = update.callback_query
  query.answer()
  query.edit_message_text(
                        text=menu_message(),
                        reply_markup=main_menu_keyboard())

def first_menu(update,context):
  query = update.callback_query
  query.answer()
  query.edit_message_text(
                        text=menu_message(),
                        reply_markup=first_menu_keyboard())

def second_menu(update,context):
  query = update.callback_query
  query.answer()
  query.edit_message_text(
                        text=menu_message(),
                        reply_markup=second_menu_keyboard())

def third_menu(update,context):
  query = update.callback_query
  query.answer()
  query.edit_message_text(
                        text=menu_message(),
                        reply_markup=third_menu_keyboard())
# and so on for every callback_data option
def first_submenu(bot, update):
  pass

def second_submenu(bot, update):
  pass

def third_submenu(bot, update):
    pass

############################ Keyboards #########################################
def main_menu_keyboard():
  keyboard = [[InlineKeyboardButton('Get Immediate Help', callback_data='m1')],
              [InlineKeyboardButton('Report Anonymously', callback_data='m2')],
              [InlineKeyboardButton('Get Information', callback_data='m3')]]
  return InlineKeyboardMarkup(keyboard)

def first_menu_keyboard():
  keyboard = [[InlineKeyboardButton('Send distress call for Michal Sela forum', callback_data='m1_1')],
              [InlineKeyboardButton('Call 911', callback_data='m1_2')],
              [InlineKeyboardButton('➡️', callback_data='main')]]
  return InlineKeyboardMarkup(keyboard)

def second_menu_keyboard():
  keyboard = [[InlineKeyboardButton('Report to Social Services', url='https://govforms.gov.il/mw/forms/MolsaContact@molsa.gov.il',
                                    callback_data='m2_1')],
              [InlineKeyboardButton('Report illegal gun', url='https://gfkt.org/%D7%98%D7%95%D7%A4%D7%A1-%D7%93%D7%99%D7%95%D7%95%D7%97-%D7%97%D7%99%D7%99%D7%9D-%D7%91%D7%A6%D7%93-%D7%A0%D7%A9%D7%A7/',
                                    callback_data='m2_2')],
              [InlineKeyboardButton('➡️', callback_data='main')]]
  return InlineKeyboardMarkup(keyboard)

def third_menu_keyboard():
  keyboard = [[InlineKeyboardButton('Warning sings in a violent relationship', url='https://www.michalsela.org.il/warning-signs',
               callback_data='m3_1')],
              [InlineKeyboardButton('Sign-up to Sayeret Michal project', url='https://www.michalsela.org.il/sayeret',
                                    callback_data='m3_2')],
              [InlineKeyboardButton('Contact Michal Sela forum', url='https://www.michalsela.org.il/contact',
                                    callback_data='m3_3')],
              [InlineKeyboardButton('➡️', callback_data='main')]]
  return InlineKeyboardMarkup(keyboard)

############################# Messages #########################################
def menu_message():
  return 'Choose an option:'

############################# Handlers #########################################

def init(dispatcher: Dispatcher):
    """Provide handlers initialization."""
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CallbackQueryHandler(main_menu, pattern='main'))
    dispatcher.add_handler(CallbackQueryHandler(first_menu, pattern='m1'))
    dispatcher.add_handler(CallbackQueryHandler(second_menu, pattern='m2'))
    dispatcher.add_handler(CallbackQueryHandler(third_menu, pattern='m3'))
    dispatcher.add_handler(CallbackQueryHandler(first_submenu,
                                                pattern='m1_1'))
    dispatcher.add_handler(CallbackQueryHandler(second_submenu,
                                                pattern='m2_1'))
    dispatcher.add_handler(CallbackQueryHandler(third_submenu,
                                                pattern='m3_1'))



# def start(update: Update, _: CallbackContext):
#     """Process a /start command."""
#     update.message.reply_text(text="I'm a bot, please talk to me!")

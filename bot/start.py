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
  update.message.reply_text(eng_menu_message(), reply_markup=language_menu_keyboard())

def language_menu(update,context):
  query = update.callback_query
  query.answer()
  query.edit_message_text(text=eng_menu_message(), reply_markup=language_menu_keyboard())

def get_help_hebrew_menu(update,context):
  query = update.callback_query
  query.answer()
  query.edit_message_text(text=heb_menu_message(), reply_markup=get_help_hebrew_menu_keyboard())

def get_help_english_menu(update,context):
  query = update.callback_query
  query.answer()
  query.edit_message_text(text=eng_menu_message(), reply_markup=get_help_english_menu_keyboard())

def get_help_arabic_menu(update,context):
  query = update.callback_query
  query.answer()
  query.edit_message_text(text=arb_menu_message(), reply_markup=get_help_arabic_menu_keyboard())

def hebrew_menu(update,context):
  query = update.callback_query
  query.answer()
  query.edit_message_text(text=heb_menu_message(), reply_markup=hebrew_menu_keyboard())

def english_menu(update,context):
  query = update.callback_query
  query.answer()
  query.edit_message_text(text=eng_menu_message(), reply_markup=english_menu_keyboard())

def arabic_menu(update,context):
  query = update.callback_query
  query.answer()
  query.edit_message_text(text=arb_menu_message(), reply_markup=arabic_menu_keyboard())

def first_submenu(bot, update):
  pass

def second_submenu(bot, update):
  pass

def third_submenu(bot, update):
    pass

############################ Keyboards #########################################
def language_menu_keyboard():
  keyboard = [[InlineKeyboardButton('עברית', callback_data='hebrew')],
              [InlineKeyboardButton('English', callback_data='english')],
              [InlineKeyboardButton('عربيه', callback_data='arabic')]]
  return InlineKeyboardMarkup(keyboard)

def hebrew_menu_keyboard():
  keyboard = [[InlineKeyboardButton('קבלי עזרה מיידית', callback_data='heb_immediate_help')],
              [InlineKeyboardButton('דיווח אנונימי', callback_data='heb_anonymous_report')],
              [InlineKeyboardButton('קבלי מידע', callback_data='heb_get_help')],
              [InlineKeyboardButton('⬅️', callback_data='language_menu_keyboard')]]
  return InlineKeyboardMarkup(keyboard)

def english_menu_keyboard():
  keyboard = [[InlineKeyboardButton('Get Immediate Help', callback_data='eng_immediate_help')],
              [InlineKeyboardButton('Report Anonymously', callback_data='eng_anonymous_report')],
              [InlineKeyboardButton('Get Information', callback_data='eng_get_help')],
              [InlineKeyboardButton('⬅️', callback_data='language_menu_keyboard')]]
  return InlineKeyboardMarkup(keyboard)

def arabic_menu_keyboard():
  keyboard = [[InlineKeyboardButton('احصل على مساعدة فورية', callback_data='arb_immediate_help')],
              [InlineKeyboardButton('تقرير مجهول', callback_data='arb_anonymous_report')],
              [InlineKeyboardButton('احصل على المعلومات', callback_data='arb_get_help')],
              [InlineKeyboardButton('⬅️', callback_data='language_menu_keyboard')]]
  return InlineKeyboardMarkup(keyboard)

def get_help_hebrew_menu_keyboard():
  keyboard = [[InlineKeyboardButton('קריאת מצוקה לפורום מיכל סלה', callback_data='heb_distress_call')],
              [InlineKeyboardButton('להתקשר למשטרה', callback_data='heb_call_police')],
              [InlineKeyboardButton('⬅️', callback_data='language_menu_keyboard')]]
  return InlineKeyboardMarkup(keyboard)

def get_help_english_menu_keyboard():
  keyboard = [[InlineKeyboardButton('Send distress call for Michal Sela forum', callback_data='eng_distress_call')],
              [InlineKeyboardButton('Call 911', callback_data='eng_call_police')],
              [InlineKeyboardButton('➡️', callback_data='language_menu_keyboard')]]
  return InlineKeyboardMarkup(keyboard)

def get_help_arabic_menu_keyboard():
  keyboard = [[InlineKeyboardButton('إرسال نداء استغاثة لمنتدى ميشال سيلا', callback_data='arb_distress_call')],
              [InlineKeyboardButton('الشرطة الدعوة', callback_data='arb_call_police')],
              [InlineKeyboardButton('➡️', callback_data='language_menu_keyboard')]]
  return InlineKeyboardMarkup(keyboard)

############################# Messages #########################################
def eng_menu_message():
  return 'Choose an option:'

def heb_menu_message():
  return 'בחרי אפשרות:'

def arb_menu_message():
  return 'إختر خيار:'
############################# Handlers #########################################

def init(dispatcher: Dispatcher):
    """Provide handlers initialization."""
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CallbackQueryHandler(language_menu, pattern='language_menu_keyboard'))
    dispatcher.add_handler(CallbackQueryHandler(hebrew_menu, pattern='hebrew'))
    dispatcher.add_handler(CallbackQueryHandler(english_menu, pattern='english'))
    dispatcher.add_handler(CallbackQueryHandler(arabic_menu, pattern='arabic'))

# def start(update: Update, _: CallbackContext):
#     """Process a /start command."""
#     update.message.reply_text(text="I'm a bot, please talk to me!")

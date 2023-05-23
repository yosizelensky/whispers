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
    update.message.reply_text('Whispers', reply_markup=language_menu_keyboard())


def language_menu(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text='Whispers', reply_markup=language_menu_keyboard())


def hebrew_get_help_menu(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=heb_menu_message(), reply_markup=hebrew_get_help_menu_keyboard())


def english_get_help_menu(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=eng_menu_message(), reply_markup=english_get_help_menu_keyboard())


def arabic_get_help_menu(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=arb_menu_message(), reply_markup=arabic_get_help_menu_keyboard())


def hebrew_supporter_form_menu(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=heb_menu_message(), reply_markup=hebrew_supporter_form_keyboard())


def english_supporter_form_menu(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=eng_menu_message(), reply_markup=english_supporter_form_keyboard())


def arabic_supporter_form_menu(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=arb_menu_message(), reply_markup=arabic_supporter_form_keyboard())

def hebrew_supported_menu(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=heb_menu_message(), reply_markup=hebrew_supported_menu_keyboard())


def english_supported_menu(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=eng_menu_message(), reply_markup=english_supported_menu_keyboard())


def arabic_supported_menu(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=arb_menu_message(), reply_markup=arabic_supported_menu_keyboard())

def hebrew_menu(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=heb_menu_message(), reply_markup=heb_service_selector_keyboard())


def english_menu(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=eng_menu_message(), reply_markup=eng_service_selector_keyboard())


def arabic_menu(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=arb_menu_message(), reply_markup=arb_service_selector_keyboard())


############################ Keyboards #########################################
def language_menu_keyboard():
    keyboard = [[InlineKeyboardButton('עברית', callback_data='hebrew')],
                [InlineKeyboardButton('English', callback_data='english')],
                [InlineKeyboardButton('عربيه', callback_data='arabic')]]
    return InlineKeyboardMarkup(keyboard)


def heb_service_selector_keyboard():
    keyboard = [[InlineKeyboardButton('תומכת', callback_data='heb_supporter')],
                [InlineKeyboardButton('נתמכת', callback_data='heb_supported')],
                [InlineKeyboardButton('⬅️', callback_data='language_menu_keyboard')]]
    return InlineKeyboardMarkup(keyboard)


def eng_service_selector_keyboard():
    keyboard = [[InlineKeyboardButton('Supporter', callback_data='eng_supporter')],
                [InlineKeyboardButton('Supported', callback_data='eng_supported')],
                [InlineKeyboardButton('⬅️', callback_data='language_menu_keyboard')]]
    return InlineKeyboardMarkup(keyboard)


def arb_service_selector_keyboard():
    keyboard = [[InlineKeyboardButton('داعم', callback_data='arb_supporter')],
                [InlineKeyboardButton('مدعوم', callback_data='arb_supported')],
                [InlineKeyboardButton('⬅️', callback_data='language_menu_keyboard')]]
    return InlineKeyboardMarkup(keyboard)

def hebrew_supported_menu_keyboard():
    keyboard = [[InlineKeyboardButton('קבלי עזרה מיידית', callback_data='heb_immediate_help')],
                [InlineKeyboardButton('דיווח אנונימי', callback_data='heb_anonymous_report')],
                [InlineKeyboardButton('קבלי מידע', callback_data='heb_get_help')],
                [InlineKeyboardButton('⬅️', callback_data='hebrew')]]
    return InlineKeyboardMarkup(keyboard)


def english_supported_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Get Immediate Help', callback_data='eng_immediate_help')],
                [InlineKeyboardButton('Report Anonymously', callback_data='eng_anonymous_report')],
                [InlineKeyboardButton('Get Information', callback_data='eng_get_help')],
                [InlineKeyboardButton('⬅️', callback_data='english')]]
    return InlineKeyboardMarkup(keyboard)


def arabic_supported_menu_keyboard():
    keyboard = [[InlineKeyboardButton('احصل على مساعدة فورية', callback_data='arb_immediate_help')],
                [InlineKeyboardButton('تقرير مجهول', callback_data='arb_anonymous_report')],
                [InlineKeyboardButton('احصل على المعلومات', callback_data='arb_get_help')],
                [InlineKeyboardButton('⬅️', callback_data='arabic')]]
    return InlineKeyboardMarkup(keyboard)


def hebrew_get_help_menu_keyboard():
    keyboard = [[InlineKeyboardButton('קריאת מצוקה לפורום מיכל סלה', callback_data='heb_distress_call')],
                [InlineKeyboardButton('להתקשר למשטרה', callback_data='heb_call_police')],
                [InlineKeyboardButton('⬅️', callback_data='language_menu_keyboard')]]
    return InlineKeyboardMarkup(keyboard)


def english_get_help_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Send distress call for Michal Sela forum', callback_data='eng_distress_call')],
                [InlineKeyboardButton('Call 911', callback_data='eng_call_police')],
                [InlineKeyboardButton('➡️', callback_data='language_menu_keyboard')]]
    return InlineKeyboardMarkup(keyboard)


def arabic_get_help_menu_keyboard():
    keyboard = [[InlineKeyboardButton('إرسال نداء استغاثة لمنتدى ميشال سيلا', callback_data='arb_distress_call')],
                [InlineKeyboardButton('الشرطة الدعوة', callback_data='arb_call_police')],
                [InlineKeyboardButton('➡️', callback_data='language_menu_keyboard')]]
    return InlineKeyboardMarkup(keyboard)


def hebrew_supporter_form_keyboard():
    keyboard = [[InlineKeyboardButton('יופיע כאן טופס', callback_data='None')],
                [InlineKeyboardButton('➡️', callback_data='hebrew')]]
    return InlineKeyboardMarkup(keyboard)


def english_supporter_form_keyboard():
    keyboard = [[InlineKeyboardButton('a form will appear here', callback_data='None')],
                [InlineKeyboardButton('➡️', callback_data='english')]]
    return InlineKeyboardMarkup(keyboard)


def arabic_supporter_form_keyboard():
    keyboard = [[InlineKeyboardButton('arabic', callback_data='None')],
                [InlineKeyboardButton('➡️', callback_data='arabic')]]
    return InlineKeyboardMarkup(keyboard)

############################# Messages #########################################
def eng_menu_message():
    return 'Choose an option:'


def eng_get_help_menu_message():
    return 'help links:'


def heb_menu_message():
    return 'בחרי אפשרות:'


def heb_get_help_menu_message():
    return 'לינקים למידע'


def arb_menu_message():
    return 'إختر خيار:'


def arb_get_help_menu_message():
    return 'احصل على المعلومات'


############################# Handlers #########################################

def init(dispatcher: Dispatcher):
    """Provide handlers initialization."""
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CallbackQueryHandler(language_menu, pattern='language_menu_keyboard'))
    dispatcher.add_handler(CallbackQueryHandler(hebrew_menu, pattern='hebrew'))
    dispatcher.add_handler(CallbackQueryHandler(english_menu, pattern='english'))
    dispatcher.add_handler(CallbackQueryHandler(arabic_menu, pattern='arabic'))
    dispatcher.add_handler(CallbackQueryHandler(hebrew_supported_menu, pattern='heb_supported'))
    dispatcher.add_handler(CallbackQueryHandler(english_supported_menu, pattern='eng_supported'))
    dispatcher.add_handler(CallbackQueryHandler(arabic_supported_menu, pattern='arb_supported'))
    dispatcher.add_handler(CallbackQueryHandler(hebrew_supporter_form_menu, pattern='heb_supporter'))
    dispatcher.add_handler(CallbackQueryHandler(english_supporter_form_menu, pattern='eng_supporter'))
    dispatcher.add_handler(CallbackQueryHandler(arabic_supporter_form_menu, pattern='arb_supporter'))

# def start(update: Update, _: CallbackContext):
#     """Process a /start command."""
#     update.message.reply_text(text="I'm a bot, please talk to me!")

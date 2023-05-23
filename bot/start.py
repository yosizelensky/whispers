# encoding: utf-8
from pprint import pprint
from logging import getLogger

from telegram import Update
from telegram.ext import CallbackContext, CommandHandler, Dispatcher, MessageHandler, Filters

# Init logger
logger = getLogger(__name__)

from telegram.ext import CommandHandler, CallbackQueryHandler, ConversationHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
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

def supported_menu(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=heb_menu_message(), reply_markup=supported_menu_keyboard(context))


def hebrew_menu(update, context):
    context.user_data['lang'] = 'heb'
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=heb_menu_message(), reply_markup=service_selector_keyboard(context))


def english_menu(update, context):
    context.user_data['lang'] = 'eng'
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=eng_menu_message(), reply_markup=service_selector_keyboard(context))


def arabic_menu(update, context):
    context.user_data['lang'] = 'arb'
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=arb_menu_message(), reply_markup=service_selector_keyboard(context))


############################ Keyboards #########################################
def language_menu_keyboard():
    keyboard = [[InlineKeyboardButton('עברית', callback_data='heb_menu')],
                [InlineKeyboardButton('English', callback_data='eng_menu')],
                [InlineKeyboardButton('عربيه', callback_data='arb_menu')]]
    return InlineKeyboardMarkup(keyboard)


def service_selector_keyboard(context):
    keyboard = [[InlineKeyboardButton(strings[context.user_data['lang']]['supporter'], callback_data='register_whisper')],
                [InlineKeyboardButton(strings[context.user_data['lang']]['supported'], callback_data=f'supported')],
                [InlineKeyboardButton('⬅️', callback_data='language_menu_keyboard')]]
    return InlineKeyboardMarkup(keyboard)


def supported_menu_keyboard(context):
    keyboard = [[InlineKeyboardButton(strings[context.user_data['lang']]['get_help'], callback_data=f'{context.user_data["lang"]}_immediate_help')],
                [InlineKeyboardButton(strings[context.user_data['lang']]['anon_report'], callback_data=f'{context.user_data["lang"]}_anonymous_report')],
                [InlineKeyboardButton(strings[context.user_data['lang']]['get_info'], callback_data=f'{context.user_data["lang"]}_get_help')],
                [InlineKeyboardButton('⬅️', callback_data=f'{context.user_data["lang"]}_menu')]]
    return InlineKeyboardMarkup(keyboard)

def get_help_menu_keyboard(context):
    keyboard = [[InlineKeyboardButton(strings[context.user_data['lang']]['distress_call'], callback_data=f'{context.user_data["lang"]}_distress_call')],
                [InlineKeyboardButton(strings[context.user_data['lang']]['call_911'], callback_data=f'{context.user_data["lang"]}_call_police')],
                [InlineKeyboardButton('⬅️', callback_data='language_menu_keyboard')]]
    return InlineKeyboardMarkup(keyboard)


def hebrew_get_help_menu_keyboard():
    keyboard = [[InlineKeyboardButton('קריאת מצוקה לפורום מיכל סלה', callback_data='heb_distress_call')],
                [InlineKeyboardButton('להתקשר למשטרה', callback_data='heb_call_police')],
                [InlineKeyboardButton('⬅️', callback_data='language_menu_keyboard')]]
    return InlineKeyboardMarkup(keyboard)


def english_get_help_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Send distress call for Michal Sela forum', callback_data='eng_distress_call')],
                [InlineKeyboardButton('Call 911', callback_data='eng_call_police')],
                [InlineKeyboardButton('⬅️', callback_data='language_menu_keyboard')]]
    return InlineKeyboardMarkup(keyboard)


def arabic_get_help_menu_keyboard():
    keyboard = [[InlineKeyboardButton('إرسال نداء استغاثة لمنتدى ميشال سيلا', callback_data='arb_distress_call')],
                [InlineKeyboardButton('الشرطة الدعوة', callback_data='arb_call_police')],
                [InlineKeyboardButton('⬅️', callback_data='language_menu_keyboard')]]
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
ANSWERING, DONE_ANSWER = range(2)

strings = {
'heb': {
    'thank_you': 'תודה רבה!',
    'please_answer_questions': 'אנא השיבי על השאלות הבאות',
    'supporter': 'תומכת',
    'supported': 'נתמכת',
    'get_help': 'קבלי עזרה מיידית',
    'anon_report': 'דיווח אנונימי',
    'get_info': 'קבלי מידע'
},
'eng': {
    'thank_you': 'Thank you!',
    'please_answer_questions': 'Please answer the following questions',
    'supporter': 'Supporter',
    'supported': 'Supported',
    'get_help': 'Get Immediate Help',
    'anon_report': 'Report Anonymously',
    'get_info': 'Get Information'
},
'arb': {
    'thank_you': 'شكرًا لك',
    'please_answer_questions': 'الرجاء الإجابة على الأسئلة التالية',
    'supporter': 'داعم',
    'supported': 'مدعوم',
    'get_help': 'احصل على مساعدة فورية',
    'anon_report': 'تقرير مجهول',
    'get_info': 'احصل على المعلومات'
}
}

questions = {
    'heb': [
      'שאלה 1',
      'שאלה 2',
    #  'Question 3',
    #  'Question 4',
    #  'Question 5',
    #  'Question 6',
    ],
    'eng':[
      'Question 1',
      'Question 2',
    #  'Question 3',
    #  'Question 4',
    #  'Question 5',
    #  'Question 6',
    ],
    'arb': [
      'سؤال 1',
      'سؤال 2',
    #  'Question 3',
    #  'Question 4',
    #  'Question 5',
    #  'Question 6',
    ]
}
current_question = 0

def register_as_whisper(update,context):
    global questions, current_question
    
    query = update.callback_query
    query.answer()
    context.bot.delete_message(
      chat_id=query.message.chat_id,
      message_id=query.message.message_id)
  
    context.bot.send_message(chat_id=query.message.chat_id, text=strings[context.user_data['lang']]['please_answer_questions'])
    context.bot.send_message(chat_id=query.message.chat_id, text=questions[context.user_data['lang']][current_question])
    current_question += 1

    return ANSWERING

def handle_register_response(update, context):
    global questions, current_question
    text = update.message.text
    if not 'answers' in context.user_data:
      context.user_data['answers'] = {}
    context.user_data['answers'][current_question] = text
    if current_question < len(questions[context.user_data['lang']]):
      update.message.reply_text(questions[context.user_data['lang']][current_question])
      current_question += 1
      return ANSWERING
    else:
      current_question = 0
      update.message.reply_text(strings[context.user_data['lang']]['thank_you'])
      pprint(context)
      pprint(context.user_data)
      # save_to_db(context)
      return ConversationHandler.END


def init(dispatcher: Dispatcher):
    """Provide handlers initialization."""
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CallbackQueryHandler(language_menu, pattern='language_menu_keyboard'))
    dispatcher.add_handler(CallbackQueryHandler(hebrew_menu, pattern='heb_menu'))
    dispatcher.add_handler(CallbackQueryHandler(english_menu, pattern='eng_menu'))
    dispatcher.add_handler(CallbackQueryHandler(arabic_menu, pattern='arb_menu'))    
    dispatcher.add_handler(CallbackQueryHandler(supported_menu, pattern='supported'))
  
    
    # Add conversation handler with the states CHOOSING, ANSWERING and TYPING_REPLY
    whisper_register_handler = ConversationHandler(
        entry_points=[CallbackQueryHandler(register_as_whisper, pattern='register_whisper')],
        states={
            ANSWERING: [MessageHandler(Filters.text,handle_register_response)],
        },
        fallbacks=[]
    )

    dispatcher.add_handler(whisper_register_handler)

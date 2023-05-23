# encoding: utf-8
from pprint import pprint
from logging import getLogger
from telegram import ParseMode

from telegram import Update
from telegram.ext import CallbackContext, CommandHandler, Dispatcher, MessageHandler, Filters

import random

# Init logger
logger = getLogger(__name__)

from telegram.ext import CommandHandler, CallbackQueryHandler, ConversationHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton


############################### Bot ############################################
def start(update, context):
    # Create a custom keyboard with location and live location buttons
    keyboard = [
        [KeyboardButton('📍Send Location📍', request_location=True)]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=False, is_persistent=True)
    
    # Send a message with the custom keyboard
    update.message.reply_text('Welcome!', reply_markup=reply_markup)
    update.message.reply_text('Whispers', reply_markup=language_menu_keyboard())


def language_menu(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=strings[context.user_data['lang']]['lang_menu_msg'], reply_markup=language_menu_keyboard())


def destruction(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=strings[context.user_data['lang']]['destruction'],
                            reply_markup=destruction_keyboard())

def supported_menu(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=strings[context.user_data['lang']]['choose_service_msg'], reply_markup=supported_menu_keyboard(context))


def hebrew_menu(update, context):
    context.user_data['lang'] = 'heb'
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=strings[context.user_data['lang']]['who_you_are'], reply_markup=service_selector_keyboard(context))


def english_menu(update, context):
    context.user_data['lang'] = 'eng'
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=strings[context.user_data['lang']]['who_you_are'], reply_markup=service_selector_keyboard(context))


def arabic_menu(update, context):
    context.user_data['lang'] = 'arb'
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=strings[context.user_data['lang']]['who_you_are'], reply_markup=service_selector_keyboard(context))


def get_help_menu(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=strings[context.user_data['lang']]['get_help_menu_msg'], reply_markup=get_help_menu_keyboard(context))


def anonymous_report_menu(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=strings[context.user_data['lang']]['anonymous_report_menu_msg'], reply_markup=anonymous_report_keyboard(context))


def get_information_menu(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=strings[context.user_data['lang']]['get_info_menu_msg'], reply_markup=get_info_menu_keyboard(context))

def distress_call_callback(update, context):
    query = update.callback_query
    username = random.choice(list(whispers.keys()))
    t_link = f'https://t.me/{username}'
    
    query.answer()
    context.bot.send_message(chat_id=query.message.chat_id, text=t_link)


############################ Keyboards #########################################
def language_menu_keyboard():
    keyboard = [[InlineKeyboardButton('עברית', callback_data='heb_menu')],
                [InlineKeyboardButton('English', callback_data='eng_menu')],
                [InlineKeyboardButton('عربيه', callback_data='arb_menu')],
                [InlineKeyboardButton('❌', callback_data='destruction')]]
    return InlineKeyboardMarkup(keyboard)


def service_selector_keyboard(context):
    keyboard = [
        [InlineKeyboardButton(strings[context.user_data['lang']]['supporter'], callback_data='register_whisper')],
        [InlineKeyboardButton(strings[context.user_data['lang']]['supported'], callback_data='supported')],
        [InlineKeyboardButton(strings[context.user_data['lang']]['x_message'], callback_data='destruction')],
        [InlineKeyboardButton('⬅️', callback_data='language_menu_keyboard')]]
    return InlineKeyboardMarkup(keyboard)


def supported_menu_keyboard(context):
    keyboard = [[InlineKeyboardButton(strings[context.user_data['lang']]['get_help'], callback_data='immediate_help')],
                [InlineKeyboardButton(strings[context.user_data['lang']]['anon_report'], callback_data='anonymous_report')],
                [InlineKeyboardButton(strings[context.user_data['lang']]['get_info'], callback_data='get_info')],
                [InlineKeyboardButton(strings[context.user_data['lang']]['emergency_numbers'], callback_data='emergency_numbers')],
                [InlineKeyboardButton(strings[context.user_data['lang']]['x_message'], callback_data='destruction')],
                [InlineKeyboardButton('⬅️', callback_data=f'{context.user_data["lang"]}_menu')]]
    return InlineKeyboardMarkup(keyboard)


def get_help_menu_keyboard(context):
    keyboard = [[InlineKeyboardButton(strings[context.user_data['lang']]['distress_call'], callback_data='distress_call')],
                [InlineKeyboardButton(strings[context.user_data['lang']]['welfare_call'], callback_data='welfare_call')],
                [InlineKeyboardButton(strings[context.user_data['lang']]['call_help'], callback_data='calling_help')],
                 [InlineKeyboardButton(strings[context.user_data['lang']]['x_message'], callback_data='destruction')],
                [InlineKeyboardButton('⬅️', callback_data='supported')]]
    return InlineKeyboardMarkup(keyboard)


def anonymous_report_keyboard(context):
    keyboard = [[InlineKeyboardButton(strings[context.user_data['lang']]['report_to_welfare'],
                                      url='https://govforms.gov.il/mw/forms/MolsaContact@molsa.gov.il', callback_data='None')],
                [InlineKeyboardButton(strings[context.user_data['lang']]['report_guns'],
                                      url='https://gfkt.org/%D7%98%D7%95%D7%A4%D7%A1-%D7%93%D7%99%D7%95%D7%95%D7%97-%D7%97%D7%99%D7%99%D7%9D-%D7%91%D7%A6%D7%93-%D7%A0%D7%A9%D7%A7/', callback_data='None')],
                [InlineKeyboardButton(strings[context.user_data['lang']]['x_message'], callback_data='destruction')],
                [InlineKeyboardButton('⬅️', callback_data='supported')]]
    return InlineKeyboardMarkup(keyboard)


def destruction_keyboard():
    keyboard = [[InlineKeyboardButton('Meatballs 🍲' , url='https://www.jessicagavin.com/grandmas-italian-meatball-recipe/', callback_data='None')],
                [InlineKeyboardButton('Lasagna 🍝', url='https://www.allrecipes.com/recipe/23600/worlds-best-lasagna/', callback_data='None')],
                [InlineKeyboardButton('Pasta 🍝', url='https://lilluna.com/spaghetti-recipe/', callback_data='None')],
                [InlineKeyboardButton('Pizza 🍕', url='https://thefoodcharlatan.com/homemade-pizza-recipe/', callback_data='None')]]
    return InlineKeyboardMarkup(keyboard)


def emergency_numbers_keyboard():

    return InlineKeyboardMarkup(keyboard)


def get_info_menu_keyboard(context):
    keyboard = [[InlineKeyboardButton(strings[context.user_data['lang']]['warning_signs'],
                                      url='https://www.michalsela.org.il/warning-signs', callback_data='None')],
                [InlineKeyboardButton(strings[context.user_data['lang']]['sayeret'],
                                      url='https://www.michalsela.org.il/sayeret', callback_data='None')],
                [InlineKeyboardButton(strings[context.user_data['lang']]['forum'],
                                      url='https://www.michalsela.org.il/contact', callback_data='None')],
                [InlineKeyboardButton(strings[context.user_data['lang']]['violent_men'],
                                      url='https://www.michalsela.org.il/contact', callback_data='violent_men')],
                [InlineKeyboardButton(strings[context.user_data['lang']]['x_message'], callback_data='destruction')],
                [InlineKeyboardButton('⬅️', callback_data='supported')]]
    return InlineKeyboardMarkup(keyboard)

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
        'get_info': 'קבלי מידע',
        'distress_call': 'קריאת מצוקה לפורום מיכל סלה',
        'call_help': 'להתקשר למוקד סיוע לנשים מוכות',
        'get_help_menu_msg': 'קבלי עזרה עכשיו!',
        'anonymous_report_menu_msg': 'דיווח אנונימי',
        'lang_menu_msg': 'בחרי שפה',
        'choose_service_msg': 'בחרי שירות',
        'who_you_are': 'מי את?',
        'report_to_welfare': 'דיווח אנונימי למשרד הרווחה',
        'report_guns': 'דיווח על נשק חם',
        'get_info_menu_msg': 'מידע',
        'warning_signs': 'סימני אזהרה בזוגיות אלימה',
        'sayeret': 'הרשמי לסיירת מיכל',
        'forum': 'צרי קשר עם פורום מיכל',
        'violent_men': 'קו סיוע לגברים אלימים',
        'welfare_call': 'קו חם של משרד הרווחה',
        'destruction': 'המתכונים האהובים עלינו',
        'x_message': '❌ ניקוי מסך'
    },
    'eng': {
        'thank_you': 'Thank you!',
        'please_answer_questions': 'Please answer the following questions',
        'supporter': 'Supporter',
        'supported': 'Supported',
        'get_help': 'Get Immediate Help',
        'anon_report': 'Report Anonymously',
        'get_info': 'Get Information',
        'distress_call': 'Send a message to Michal Sela forum',
        'call_help': 'Domestic Violence Hotline',
        'get_help_menu_msg': 'Get help now!',
        'anonymous_report_menu_msg': 'Anonymous Report',
        'lang_menu_msg': 'Choose a language',
        'choose_service_msg': 'Choose service',
        'who_you_are': 'Who you are?',
        'report_to_welfare': 'Anonymous Report to Ministry of Welfare',
        'report_guns': 'Report guns',
        'get_info_menu_msg': 'Information',
        'warning_signs': 'Warning signs of a violent relationship',
        'sayeret': 'Sign-up to Sayeret Michal',
        'forum': 'Contact Michal Sela forum',
        'violent_men': 'Assistance for violent men',
        'welfare_call': 'Ministry of Welfare hotline',
        'destruction': 'Our favourite recepies',
        'x_message': '❌ Clear the screen'
    },
    'arb': {
        'thank_you': 'شكرًا لك',
        'please_answer_questions': 'الرجاء الإجابة على الأسئلة التالية',
        'supporter': 'داعم',
        'supported': 'مدعوم',
        'get_help': 'احصل على مساعدة فورية',
        'anon_report': 'تقرير مجهول',
        'get_info': 'احصل على المعلومات',
        'distress_call': 'إرسال نداء استغاثة لمنتدى ميشال سيلا',
        'call_help': 'خطوط طوارئ للنساء المعنفات',
        'get_help_menu_msg': 'الحصول على مساعدة الآن!',
        'anonymous_report_menu_msg': 'تقرير مجهول',
        'lang_menu_msg': 'اختر لغة',
        'choose_service_msg': 'اختر الخدمة',
        'who_you_are': 'من أنت',
        'report_to_welfare': 'تقرير مجهول إلى وزارة الرفاه',
        'report_guns': 'تقرير البنادق',
        'get_info_menu_msg': 'معلومة',
        'warning_signs': 'علامات التحذير من وجود علاقة عنيفة',
        'sayeret': 'الاشتراك في Sayeret Michal',
        'forum': 'تواصل مع منتدى ميشال سيلا',
        'violent_men': 'مساعدة الرجال العنيفين',
        'welfare_call': 'الخط الساخن لوزارة الرفاه',
        'destruction': 'الوصفات المفضلة لدينا',
        'x_message': '❌ امسح الشاشة'
    }
}

questions = {
    "heb":
    [
        "שם",
        "עיר מגורים",
        "טלפון",
        "הכשרה? (עורכת דין, יועצת כלכלית, עובדת סוציאלית, יועצת זוגיות, פסיכולוגית, רופאה, אין לי הכשרה בתחומים אלה)",
        "מה ההיכרות שלך עם נושא האלימות במשפחה? (אישי, מקצועי, ללא היכרות כלל)"
    ],
    "eng":
    [
        "Name",
        "Hometown",
        "phone",
        "training? (Lawyer, financial advisor, social worker, relationship counselor, psychologist, doctor, I have no training in these fields)",
        "How familiar are you with the issue of domestic violence? (personal, professional, no introduction at all)"
    ],
    "arb":
    [
        "اسم",
        "مسقط رأس",
        "هاتف",
        "تدريب؟ (محام ، مستشار مالي ، أخصائي اجتماعي ، مستشار علاقات ، طبيب نفساني ، طبيب ، ليس لدي تدريب في هذه المجالات) ",
        "ما مدى معرفتك بقضية العنف المنزلي؟ (شخصية ، مهنية ، لا مقدمة على الإطلاق)"
    ]
}

current_question = 0

whispers = {}

def save_to_db(username, user_data):
    whispers[username] = user_data

def register_as_whisper(update, context):
    global questions, current_question

    query = update.callback_query
    query.answer()
    context.bot.delete_message(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id)

    context.bot.send_message(chat_id=query.message.chat_id,
                             text=strings[context.user_data['lang']]['please_answer_questions'])
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
        save_to_db(update.effective_user.username, context.user_data)
        return ConversationHandler.END

def calling_help(update, context):
    query = update.callback_query
    query.answer()
    context.bot.send_message(chat_id=query.message.chat_id, text='No2Violence: 1-800-353-300')


def calling_welfare(update, context):
    query = update.callback_query
    query.answer()
    context.bot.send_message(chat_id=query.message.chat_id, text='Ministry of Welfare hotline: 077-9208560')

def violent_men_hotline(update, context):
    query = update.callback_query
    query.answer()
    context.bot.send_message(chat_id=query.message.chat_id, text='Wizo: 1-800-393-904')

# Handler for receiving location updates
def location_handler(update, context):
    location = update.message.location
    update.message.reply_text(f'Your location: {location.latitude}, {location.longitude}')

def init(dispatcher: Dispatcher):
    """Provide handlers initialization."""
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CallbackQueryHandler(language_menu, pattern='language_menu_keyboard'))
    dispatcher.add_handler(CallbackQueryHandler(hebrew_menu, pattern='heb_menu'))
    dispatcher.add_handler(CallbackQueryHandler(english_menu, pattern='eng_menu'))
    dispatcher.add_handler(CallbackQueryHandler(arabic_menu, pattern='arb_menu'))
    dispatcher.add_handler(CallbackQueryHandler(supported_menu, pattern='supported'))
    dispatcher.add_handler(CallbackQueryHandler(get_help_menu, pattern='immediate_help'))
    dispatcher.add_handler(CallbackQueryHandler(anonymous_report_menu, pattern='anonymous_report'))
    dispatcher.add_handler(CallbackQueryHandler(distress_call_callback, pattern='distress_call'))
    dispatcher.add_handler(CallbackQueryHandler(calling_help, pattern='calling_help'))
    dispatcher.add_handler(CallbackQueryHandler(calling_welfare, pattern='welfare_call'))
    dispatcher.add_handler(CallbackQueryHandler(get_information_menu, pattern='get_info'))
    dispatcher.add_handler(CallbackQueryHandler(destruction, pattern='destruction'))
    dispatcher.add_handler(CallbackQueryHandler(emergency_numbers_keyboard, pattern='emergency_numbers'))

    # Add conversation handler with the states CHOOSING, ANSWERING and TYPING_REPLY
    whisper_register_handler = ConversationHandler(
        entry_points=[CallbackQueryHandler(register_as_whisper, pattern='register_whisper')],
        states={
            ANSWERING: [MessageHandler(Filters.text, handle_register_response)],
        },
        fallbacks=[]
    )

    dispatcher.add_handler(whisper_register_handler)
    dispatcher.add_handler(MessageHandler(Filters.location, location_handler))

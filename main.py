import telebot
import schedule
import time
from telebot import types

bot = telebot.TeleBot("5886727201:AAGekZQdKSHbGLq0kQDQbbsAflmvzifOmJU")

class Info:
    def __init__(self):
        self.chat = 0
        self.chatid = {}  
        self.status = {}  

    def reminder(self, userid, resp, ind):
        self.chatid[userid][ind] = resp  


info = Info()

@bot.message_handler(commands=['start'])
def send_keyboard(msg):
    info.chat = msg.chat.id
    if msg.chat.id in info.chatid.keys():
        pass
    else:
        info.chatid[msg.chat.id] = [0]*5
        info.status[msg.chat.id] = [0]*5
        bot.send_message(chat_id=msg.chat.id,
                        text='Привет! Я был обещан Вике Зайцевой как напоминание о том,'
                        'что она должна записаться на танцы. Я очень назойлив. \n'
                        'Хвалить и ругать за меня можно Надю Кондратьеву.',
                        parse_mode='Markdown')

    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('Включить уведмления')
    itembtn2 = types.KeyboardButton('Выключить уведомления')
    keyboard.add(itembtn1, itembtn2)
    msg = bot.send_message(msg.from_user.id,
                           text='Выбери, что делать с уведомлениями 👇',
                           reply_markup=keyboard)

    bot.register_next_step_handler(msg, mainfunction)

def mainfunction(call):
    if call.text == "Включить уведмления":
        enable_notifications(call)
    elif call.text == "Выключить уведомления":
        turn_off_notifications(call)

def enable_notifications(call):
    keyboard = types.ReplyKeyboardMarkup(row_width=1)
    itembtn11 = types.KeyboardButton('На 9:00')
    itembtn21 = types.KeyboardButton('На 12:00')
    itembtn31 = types.KeyboardButton('На 15:00')
    itembtn41 = types.KeyboardButton('На 18:00')
    itembtn51 = types.KeyboardButton('На 21:00')
    itembtn15 = types.KeyboardButton('Вернуться назад')
    keyboard.add(itembtn11, itembtn21)
    keyboard.add(itembtn31, itembtn41)
    keyboard.add(itembtn51, itembtn15)
    msg = bot.send_message(call.from_user.id,
                           text='Выбери время',
                           reply_markup=keyboard)
    bot.register_next_step_handler(msg, callback_worker_enable)

def callback_worker_enable(call):
    if call.text == 'На 9:00':
        resp = True
        info.reminder(call.chat.id, resp, 0)
        schedule.every().day.at("09:00").do(nine_am_message)
        bot.send_message(chat_id=call.chat.id, text='Уведомления наа 9 утра успешно включены!\n',
                    parse_mode='Markdown')
        enable_notifications(call)

    elif call.text == 'На 12:00':
        resp = True
        info.reminder(call.chat.id, resp, 1)
        schedule.every().day.at("12:00").do(twelve_am_message)
        bot.send_message(chat_id=call.chat.id, text='Уведомления на 12 дня успешно включены!\n',
                    parse_mode='Markdown')
        enable_notifications(call)

    elif call.text == 'На 15:00':
        resp = True
        info.reminder(call.chat.id, resp, 2)
        schedule.every().day.at("15:00").do(three_pm_message)
        bot.send_message(chat_id=call.chat.id, text='Уведомления на 15 дня успешно включены!\n',
                    parse_mode='Markdown')
        enable_notifications(call)

    elif call.text == 'На 18:00':
        resp = True
        info.reminder(call.chat.id, resp, 3)
        schedule.every().day.at("18:00").do(six_pm_message)
        bot.send_message(chat_id=call.chat.id, text='Уведомления на 6 вечера успешно включены!\n',
                    parse_mode='Markdown')
        enable_notifications(call)

    elif call.text == 'На 21:00':
        resp = True
        info.reminder(call.chat.id, resp, 4)
        schedule.every().day.at("21:00").do(nine_pm_message)
        bot.send_message(chat_id=call.chat.id, text='Уведомления наа 9 вечера успешно включены!\n',
                    parse_mode='Markdown')
        enable_notifications(call)
    else:
        send_keyboard(call)

def nine_am_message():
    bot.send_message(chat_id=info.chat, text='Солнышко, ты уже проснулось?) \n'
                    'Молодец, а ты записалась на танцы? Нет???????? Не молодец!!! Иди записывайся',
                     parse_mode='Markdown')
def twelve_am_message():
    bot.send_message(chat_id=info.chat, text='Уже 12 дня, а ты все еще не записалась на танцы!!! \n'
                    'Нехорошо, нехорошо!!! Такими темпами из солнышка я превращаюсь  в грозовую тучку!!!',
                     parse_mode='Markdown')
def three_pm_message():
    bot.send_message(chat_id=info.chat, text='Не зли меня, запишись на танцы, уже 3 часа дня!!! \n'
                    'Я жду, очень жду',
                     parse_mode='Markdown')
def six_pm_message():
    bot.send_message(chat_id=info.chat, text='Все еще жду, надеюсь и верю, что ты запишешься на танцы \n'
                    'Пора, мой друг, пора, свободу дай плененному телу, навстречу блеску сафитов звездой танцпола явись!',
                     parse_mode='Markdown')
def nine_pm_message():
    bot.send_message(chat_id=info.chat, text='Ты записалась на танцы? \n'
                    'Ну я знаю, что не записалась, похоже сегодня я стану твоим ночным кошмаром',
                     parse_mode='Markdown')

def turn_off_notifications(call):
    for i in range(5):
        info.reminder(call.chat.id, 0, i)
    schedule.clear()
    bot.send_message(chat_id=call.chat.id, text='Очень жаль 😢\nЯ надеюсь, это связано с тем,'
                                                'что ты все-таки записалась на танцы',
                        parse_mode='Markdown')
    send_keyboard(call)

bot.polling(none_stop=True)
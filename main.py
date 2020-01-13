import telebot
from decouple import config

bot = telebot.TeleBot(config('API_TOKEN'))

start_keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
start_keyboard.row('Записаться')

status = 0
dates = []

#Start chatting with bot 
@bot.message_handler(commands=['start'])
def start_message(message):
    status = 0
    bot.send_message(message.chat.id, f"""Рады приветсвовать тебя в нашем боте.Он поможет тебе записаться к врачу хириргу-онкогинекологу Михаилу Александровичу""", reply_markup=start_keyboard)

#Message handler
@bot.message_handler(content_types=['text'])
def resolve(message):
    if message.text == 'Записаться':
        bot.send_message(message.chat.id, "Введите дату начала записи")
    else:
        if dates == []:
            status = 1 
            check_in(message, status)
        else:
            status = 2
            check_in(message, status)
#Base functions 
def check_in(message, status):
    if status == 1:
        print('Start date: {}'.format(message.text))
    elif: status == 2: 
        print('End date: {}'.format(message.text))

bot.polling()
import telebot
from decouple import config

bot = telebot.TeleBot(config('API_TOKEN'))

start_keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
start_keyboard.row('Записаться')

status = 0

#Start chatting with bot 
@bot.message_handler(commands=['start'])
def start_message(message):
    status = 0
    bot.send_message(message.chat.id, f"""Рады приветсвовать тебя в нашем боте.Он поможет тебе записаться к врачу хириргу-онкогинекологу Михаилу Александровичу""", reply_markup=start_keyboard)

#Message handler
@bot.message_handler(content_types=['text'])
def resolve(message):
    if message.text == 'Записаться':
        status = 1
        bot.send_message(message.chat.id, "Введите дату начала записи")
    else:
        check_in(message)

#Base functions 
def check_in(message):
    print("We're in check in function")  #TODO time start and end check in 


bot.polling()
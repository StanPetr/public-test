import telebot
from config import keys, TOKEN
from utils import ConvertionExeption, CryptoConverter

bot=telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text='Чтобы начать работу введите комманду боту в следующем формате:\n' \
'<наименование валюты>\<в какую валюту перевести>\
<количество денежных единиц>\n Посмотреть список всех доступных валют: /values'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message:telebot.types.Message):
    text='Доступные валюты:'
    for key in keys.keys():
        '\n'.join((text,key,))
    bot.reply_to(message,text)


@bot.message_handler(content_types=['text', ])
def convert(message:telebot.types.Message):
    values= message.text.split(' ')

    if len(values) != 3:
        raise ConvertionExeption('Слишком много параметров.')

    quote, base, ammount = values
    total_base = CryptoConverter.convert(quote, base, ammount)

    text = f'Цена {ammount} {quote} в {base} - {total_base}'
    bot.send_message(message.chat.id, text)

bot.polling()
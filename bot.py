import config
import utils
from utils import ConvertionException, CryptoConverter
import telebot
from config import keys,TOKEN

bot = telebot.TeleBot(TOKEN)



@bot.message_handler(commands=['start', 'help'])

def help(message: telebot.types.Message):
    bot.send_message(message.chat.id,("Чтобы начать работу введите команду боту в формате:"
                                      "\n <имя валюты> "
                                      "\n <в какую валюту перевести> "
                                      "\n <количество переводимой валюты>"
                                      "Увидеть все доступные валюты /values"))



@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    total_base = CryptoConverter.convert(quote, base, amount)

    text = f'Цена {amount} {quote} в {base} - {total_base}'
    bot.send_message(message.chat.id,text)

bot.polling()

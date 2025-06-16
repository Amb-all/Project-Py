import telebot
from library import requests, json
from config import keys, TOKEN

bot = telebot.TeleBot(TOKEN)

class Conversionexception(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def convert(self):
        pass

@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = ('Чтобы начать работу введите команду боту в следующем формате'
            ':\n<имя исходной валюты> <в какую валюту перевести> <количество переводимой валюты>'
            '\nПример: "доллар рубль 1"\n\nУвидеть список доступных валют, введите команду: /values')
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text += f'\n-> {key}'
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    try:
        quote, base, amount = message.text.split(' ')

        # Проверяем, что валюты поддерживаются
        if quote not in keys:
            raise ValueError(f"Валюта {quote} не поддерживается.")
        if base not in keys:
            raise ValueError(f"Валюта {base} не поддерживается.")

        quote_ticker = keys[quote]
        base_ticker = keys[base]

        # Делаем запрос к API
        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[base_ticker]

        # Рассчитываем стоимость
        result = total_base * float(amount)
        text = f'Цена {amount} {quote} в {base}: {result:.2f} {base_ticker}'
        bot.send_message(message.chat.id, text)

    except ValueError as e:
        bot.reply_to(message, f'Ошибка ввода: {e}\n Проверьте формат ввода.')
    except Exception as e:
        bot.reply_to(message, f"Произошла ошибка: {e}")


bot.polling()
import telebot
import requests
import json

data = json.loads(
    requests.get("http://api.exchangeratesapi.io/v1/latest?access_key=c80bb83b35a335d5c2e6b281107fca10&source=USD").text)
data["rates"].update((key, round(val, 2)) for key, val in data["rates"].items())
x: object = (data.get("rates"))


res = data['base'] + '\n' + '\n'.join([f'{key}: {value}' for key, value in data['rates'].items()])


token = '2027306950:AAGMeiEv6qtuxMLMevAlkgpqjXXnKLicfu0'
bot = telebot.TeleBot(token)


@bot.message_handler(content_types=['text'])
def xsddsq(message):
    if message.chat.type == 'private':
        if message.text == 'start' or message.text == '/start':
            bot.send_message(message.chat.id, 'Send command /list or /lst to see currenices for now')
        elif message.text in ('list', 'lst', '/list', '/lst'):
            bot.send_message(message.chat.id, (res))
        elif message.text == 'history for USD/CAD 7 days' or message.text == '/history for USD/CAD 7 days':
            bot.send_message(message.chat.id, 'You Have No Permission To Do This')
        else:
            bot.send_message(message.chat.id, 'Send Command For Me')




bot.polling(none_stop=True)



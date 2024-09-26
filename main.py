import telebot
from telebot import types
from forward import API_TOKEN

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def startfunc(message):
    bot.send_message(message.chat.id,"Assalom alaykum")




@bot.message_handler(content_types=['text'])
def messagefunc(message):
    if message.text == '1':
        bot.send_video(message.chat.id,"https://t.me/adix7pro/110",caption="Kino kodi : 1\n Kino nomi : Kung Fu Panda 1")
    elif message.text == '2':
        bot.send_video(message.chat.id,"https://t.me/adix7pro/111",caption= "Kino kodi : 2\n Kino nomi : Hacker")
    else:
        bot.send_message(message.chat.id,"Bunday kodga ega raqam mavjud emas")
    
bot.polling(none_stop=True)
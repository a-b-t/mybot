"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход 
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите 
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите 
  бота отвечать, в каком созвездии сегодня находится планета.

"""


from glob import glob
import logging
from random import choice

from emoji import emojize
import ephem
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings

logging.basicConfig(format = '%(asctime)s - %(levelname)s - %(message)s',
                    level = logging.INFO,
                    filename = 'bot.log')


def greet_user(bot, update, user_data):
    smile = get_user_emo(user_data)
    user_data['smile'] = smile
    text = 'Привет {}'.format(smile)
    update.message.reply_text(text)

def talk_to_me(bot, update, user_data):
    smile = get_user_emo(user_data)
    user_text = "Привет {} {}! Ты написал: {}".format(update.message.chat.first_name, user_data["smile"], update.message.text)
    logging.info('User: %s, Chat id: %s, Message: %s', update.message.chat.username, 
    update.message.chat.id, update.message.text)
    update.message.reply_text(user_text)

def planet_name(bot, update, user_data):
    planet_name = update.message.text.split()[1]
    date = ephem.now()
    planet = getattr(ephem, planet_name)(date)
    const = ephem.constellation(planet)
    text = f'Сегодня планета {planet_name} находится в созвездии {const[1]}'
    update.message.reply_text(text)

def wordcount(bot, update, user_data):
    words = update.message.text.split()[1:]
    if words != []:
        answer = "{} слова".format(len(words))
    else:
        answer = 'Забыл ввести фразу!'
    update.message.reply_text(answer)

def next_full_moon(bot, update, user_data):
    date = ephem.now()
    text = 'Ближайшее полнолуние будет {}'.format(ephem.next_full_moon(date))
    update.message.reply_text(text)

def send_cat_picture(bot, update, user_data):
    cat_list = glob('images/cat*.jp*g')
    cat_pic = choice(cat_list)
    bot.send_photo(chat_id=update.message.chat.id, photo=open(cat_pic, 'rb'))

def get_user_emo(user_data):
    if 'smile' in user_data:
        return user_data['smile']
    else:
        user_data['smile'] = emojize(choice(settings.USER_EMOJI), use_aliases=True)
        return user_data['smile']


def main():
    mybot = Updater(settings.API_KEY, request_kwargs = settings.PROXY)
    logging.info('Бот запускается')    
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user, pass_user_data=True))
    dp.add_handler(CommandHandler('cat', send_cat_picture, pass_user_data=True))
    dp.add_handler(CommandHandler('planet', planet_name, pass_user_data=True))
    dp.add_handler(CommandHandler('wordcount', wordcount, pass_user_data=True))
    dp.add_handler(CommandHandler('next_full_moon', next_full_moon, pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me, pass_user_data=True))
    
    mybot.start_polling()
    mybot.idle()
       

if __name__ == "__main__":
    main()

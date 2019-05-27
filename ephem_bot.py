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

import logging
import settings
import ephem
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format = '%(asctime)s - %(levelname)s - %(message)s',
                    level = logging.INFO,
                    filename = 'bot.log')


def greet_user(bot, update):
    text = 'Вызван /start'
    logging.info(text)
    update.message.reply_text(text)

def talk_to_me(bot, update):
    user_text = "Привет {}! Ты написал: {}".format(update.message.chat.first_name, update.message.text)
    logging.info('User: %s, Chat id: %s, Message: %s', update.message.chat.username, 
    update.message.chat.id, update.message.text)
    update.message.reply_text(user_text)

def planet_name(bot, update):
    planet_name = update.message.text.split()[1]
    date = ephem.now()
    planet = getattr(ephem, planet_name)(date)
    const = ephem.constellation(planet)
    text = f'Сегодня планета {planet_name} находится в созвездии {const[1]}'
    update.message.reply_text(text)

def wordcount(bot, update):
    words = update.message.text.split()[1:]
    if words != []:
        answer = "{} слова".format(len(words))
    else:
        answer = 'Забыл ввести фразу!'
    update.message.reply_text(answer)

def next_full_moon(bot, update):
    date = ephem.now()
    text = 'Ближайшее полнолуние будет {}'.format(ephem.next_full_moon(date))
    update.message.reply_text(text)

def main():
    mybot = Updater(settings.API_KEY, request_kwargs = settings.PROXY)
    logging.info('Бот запускается')    
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(CommandHandler('planet', planet_name))
    dp.add_handler(CommandHandler('wordcount', wordcount))
    dp.add_handler(CommandHandler('next_full_moon', next_full_moon))
    mybot.start_polling()
    mybot.idle()
       

if __name__ == "__main__":
    main()

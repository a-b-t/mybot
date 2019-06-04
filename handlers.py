from glob import glob
from random import choice

import logging
import ephem

from utils import get_keyboard, get_user_emo

def greet_user(bot, update, user_data):
    smile = get_user_emo(user_data)
    user_data['smile'] = smile
    text = 'Привет {}'.format(smile)
    update.message.reply_text(text, reply_markup=get_keyboard())

def get_contact(bot, update, user_data):
    print(update.message.contact)
    update.message.reply_text('Готово: {}'.format(get_user_emo(user_data)), reply_markup=get_keyboard())

def get_location(bot, update, user_data):
    print(update.message.location)
    update.message.reply_text('Готово: {}'.format(get_user_emo(user_data)), reply_markup=get_keyboard())



def talk_to_me(bot, update, user_data):
    smile = get_user_emo(user_data)
    user_text = "Привет {} {}! Ты написал: {}".format(update.message.chat.first_name, user_data["smile"], update.message.text)
    logging.info('User: %s, Chat id: %s, Message: %s', update.message.chat.username, 
    update.message.chat.id, update.message.text)
    update.message.reply_text(user_text, reply_markup=get_keyboard())

def planet_name(bot, update, user_data):
    planet_name = update.message.text.split()[1]
    date = ephem.now()
    planet = getattr(ephem, planet_name)(date)
    const = ephem.constellation(planet)
    text = f'Сегодня планета {planet_name} находится в созвездии {const[1]}'
    update.message.reply_text(text, reply_markup=get_keyboard())

def wordcount(bot, update, user_data):
    words = update.message.text.split()[1:]
    if words != []:
        answer = "{} слова".format(len(words))
    else:
        answer = 'Забыл ввести фразу!'
    update.message.reply_text(answer, reply_markup=get_keyboard())

def next_full_moon(bot, update, user_data):
    date = ephem.now()
    text = 'Ближайшее полнолуние будет {}'.format(ephem.next_full_moon(date))
    update.message.reply_text(text, reply_markup=get_keyboard())

def send_cat_picture(bot, update, user_data):
    cat_list = glob('images/cat*.jp*g')
    cat_pic = choice(cat_list)
    bot.send_photo(chat_id=update.message.chat.id, photo=open(cat_pic, 'rb'), reply_markup=get_keyboard())

def change_avatar(bot, update, user_data):
    if 'smile' in user_data:
        del user_data['smile']
    smile = get_user_emo(user_data)
    update.message.reply_text('Готово: {}'.format(smile), reply_markup=get_keyboard())

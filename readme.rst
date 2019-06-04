AstroCatBot
============

AstroCatBot - это бот для Telegram 

Установка
-----------

Создайте виртуальное окружение и активируйте его. Потом в виртуальном окружении выполните:

.. code-block:: text

    pip install -r requirements.text

Положите картинки с котиками в папку images. Название файлов должно начинаться с cat, а заканчиваться .jpg, например cat8999.jpg.

Настройка
-------------

Создайте файл settins.py и добавьте туда следующие настройки:

.. code-block:: python

    PROXY = {'proxy_url': 'socks5h://ВАШ_SOCKS5_ПРОКСИ:1080', 
            'urllib3_proxy_kwargs': {'username': 'ЛОГИН', 'password': 'ПАРОЛЬ'}}
    API_KEY = "API ключ, который вы получили у BotFather"

    USER_EMOJI = [':smiley_cat:', ':smiling_imp:', ':panda_face:', ':dog:']

Запуск
--------------

В активированном виртуальном окружении выполните:

.. code-block:: text

    python3 learn_bot.py
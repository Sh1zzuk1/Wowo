import telebot
from telebot import types
import json

API_TOKEN = '7384757316:AAGrTA66ZXXYCyGSkhUtO_hzUn0XHpaLDRM'
bot = telebot.TeleBot(API_TOKEN)

# Пример хранилища для хранения данных пользователей
user_data_storage = {}


def check_registration_status(user_id):
    return user_id in user_data_storage


@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id
    if check_registration_status(user_id):
        bot.send_message(
            message.chat.id,
            "Вы уже зарегистрированы! Переходите на сайт для дальнейшего использования.",
            reply_markup=types.InlineKeyboardMarkup().row(
                types.InlineKeyboardButton('Перейти на сайт', web_app=types.WebAppInfo(
                    url='https://sh1zzuk1.github.io/submit_registration'))
            )
        )
    else:
        bot.send_message(
            message.chat.id,
            "Добро пожаловать в лучшее приложение для знакомств, в котором вы можете найти себе пару, друга и т.д."
            "\nМы предоставим вам людей, живущих прямо в вашем городе, вам остается только пройти регистрацию!"
            "\nДля этого нажмите на кнопку открыть Wowo",
            reply_markup=types.InlineKeyboardMarkup().row(
                types.InlineKeyboardButton('Открыть Wowo',
                                           web_app=types.WebAppInfo(url='https://sh1zzuk1.github.io/Wowo/'))
            )
        )


@bot.message_handler(content_types=['web_app_data'])
def handle_web_app_data(message):
    data = message.web_app_data.data
    user_data = json.loads(data)
    name = user_data['name']
    age = user_data['age']
    about = user_data['about']

    user_id = message.from_user.id
    user_data_storage[user_id] = user_data

    bot.send_message(
        message.chat.id,
        f"Ваши данные\nИмя: {name}, {age} лет, описание: {about}"
    )


bot.polling()

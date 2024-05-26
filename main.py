import telebot

API_TOKEN = '7384757316:AAGrTA66ZXXYCyGSkhUtO_hzUn0XHpaLDRM'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(
        message.chat.id,
        "Добро пожаловать в лучшее приложение для знакомств в котором вы можете найти себе, пару, друга и т.д. "
            "\n мы предоставим вам людей живущих прямо в вашем городе, вам остается только пройти регистрацию!"
            "\n Для этого нажмите на кнопку открыть Wowo",
        reply_markup=telebot.types.InlineKeyboardMarkup().row(
            telebot.types.InlineKeyboardButton('Открыть Wowo', web_app=telebot.types.WebAppInfo(url='https://your-web-app-url.com'))
        )
    )

bot.polling()
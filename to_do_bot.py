from telebot import TeleBot, types
import random

bot = TeleBot(token='token', parse_mode='html') # создание бота

book = ['Эдвард Деминг "О качествах и процессах"','Гленфорд Майерс "О тестировании"','Ли Коупленд "О технологиях тест-дизайна"','Рекс Блэк "О тест-менеджменте"']
video = ['https://www.youtube.com/watch?v=8eH3k4BxV6k','https://www.youtube.com/watch?v=XmAlTpcdNeA','https://www.youtube.com/watch?v=cFW2MfR-a88','https://www.youtube.com/watch?v=PHwEikZezUY','https://www.youtube.com/watch?v=FkhWIgqtmZ8','https://www.youtube.com/watch?v=tNmXasA2wpg&t=1s','https://www.youtube.com/watch?v=_Z62E46bDmY']

# обработчик команды '/start'
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Сегодня я ленивец")
    btn2 = types.KeyboardButton("Готов учиться!")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Чем займемся сегодня?🤔".format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "Сегодня я ленивец"):
        bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEGLxNjVZSFOAXWdgABd8FlTTdVNI01eQwAAj0IAAL6C7YIDFmCi4hnr9AqBA")
    elif(message.text == "Готов учиться!"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Что почитать?📚")
        btn2 = types.KeyboardButton("Что посмотреть?📺")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Задай мне вопрос", reply_markup=markup)
    
    elif(message.text == "Что почитать?📚"):
        msg = random.choice(book)
        bot.send_message(message.chat.id, msg)
    
    elif message.text == "Что посмотреть?📺":
        vdo = random.choice(video)
        bot.send_message(message.chat.id, vdo)
    
    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Сегодня я ленивец")
        button2 = types.KeyboardButton("Готов учиться!")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="Ошибочка вышла, попробуй еще раз")

bot.polling(none_stop=True)

# главная функция программы
def main():
    # запускаем нашего бота
    bot.infinity_polling()


if __name__ == '__main__':
    main()

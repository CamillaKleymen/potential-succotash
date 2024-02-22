import telebot
import transbuttons

bot = telebot.TeleBot('7134520910:AAG-fD5HkFrrqiXLvxQNtUHa8IPe_78Hw60')


@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    bot.send_message(user_id, "Shalom! I'll be your best translator!", reply_markup=transbuttons.main_menu())
    bot.register_next_step_handler(message, translate)


def translate(message):
    user_id = message.from_user.id
    if message.text.lower() == 'translate':
        bot.send_message(user_id, 'OK, enter a word and language to translate (ENG-RU): ')
        bot.register_next_step_handler(message, process_translation)
    elif message.text.lower() == 'wikipedia':
        bot.send_message(user_id, 'What do you want to know about?')
        bot.register_next_step_handler(message, search_process)
    else:
        bot.send_message(user_id, message.text)


def process_translation(message):
    user_id = message.from_user.id
    bot.send_message(user_id, 'Translation processing...')
    bot.register_next_step_handler(message, search_process)
def search_process(message):
    user_id = message.from_user.id
    bot.send_message(user_id, 'Search processing...')


bot.polling(non_stop=True)

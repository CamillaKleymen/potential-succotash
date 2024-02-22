import telebot
import converterbuttons

bot = telebot.TeleBot('6581341478:AAEoHaXaYT4sQSESr08SMUuDSDsVz2gAUV4')

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    bot.send_message(user_id, 'Hello, what currency do you want to convert?', reply_markup=converterbuttons.main_menu())
    bot.register_next_step_handler(message, ask_amount)

while True:
    def ask_amount(message):
        user_id = message.from_user.id
        currency = message.text.lower()
        bot.send_message(user_id, 'Enter the amount you want to convert:')
        bot.register_next_step_handler(message, lambda msg: convert(msg, currency))

    def convert(message, currency):
        user_id = message.from_user.id
        amount = float(message.text)
        if currency == 'rub':
            converted_amount = amount * 100
        elif currency == 'euro':
            converted_amount = amount * 15000
        elif currency == 'usd':
            converted_amount = amount * 12000
        else:
            bot.send_message(user_id, 'Unsupported currency')
            return
        bot.send_message(user_id, f'Converted amount: {converted_amount} {currency.upper()}')

bot.polling()

from telebot import types

def main_menu():
    cv = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('RUB')
    button2 = types.KeyboardButton('EURO')
    button3 = types.KeyboardButton('USD')
    cv.add(button1, button2, button3)
    return cv


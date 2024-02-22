from telebot import types

def main_menu():
    tc = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('translate')
    button2 = types.KeyboardButton('wikipedia')
    tc.add(button1, button2)
    return tc

from telebot.types import*


def ugvip_btn():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    admin = types.KeyboardButton(text="Admin",)
    mm = types.KeyboardButton(text="Mobile Money",)
    chipper = types.KeyboardButton(text="Chipper Cash",)
    card = types.KeyboardButton(text="Card 💳",)
    markup.add(mm,chipper,card)
    markup.add(admin)
    return markup

def kevip_btn():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    admin = types.KeyboardButton(text="Admin",)
    mm = types.KeyboardButton(text="MTN mpesa",)
    chipper = types.KeyboardButton(text="Chipper Cash",)
    card = types.KeyboardButton(text="Card 💳",)
    markup.add(mm,chipper,card)
    markup.add(admin)
    return markup


def ghvip_btn():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    chipper = types.KeyboardButton(text="Chipper Cash",)
    card = types.KeyboardButton(text="Card 💳",)
    markup.add(chipper,card)
    return markup

def rwvip_btn():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    mm = types.KeyboardButton(text="Admin",)
    chipper = types.KeyboardButton(text="Chipper Cash",)
    card = types.KeyboardButton(text="Card 💳",)
    markup.add(chipper,card)
    markup.add(mm)
    return markup

def tzvip_btn():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    mm = types.KeyboardButton(text="Admin",)
    chipper = types.KeyboardButton(text="Chipper Cash",)
    card = types.KeyboardButton(text="Card 💳",)
    markup.add(chipper,card)
    markup.add(mm)
    return markup

def nivip_btn():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    mm = types.KeyboardButton(text="Admin",)
    chipper = types.KeyboardButton(text="Chipper Cash",)
    card = types.KeyboardButton(text="Card 💳",)
    markup.add(chipper,card)
    markup.add(mm)
    return markup

def usavip_btn():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    mm = types.KeyboardButton(text="Admin",)
    chipper = types.KeyboardButton(text="Chipper Cash",)
    card = types.KeyboardButton(text="Card 💳",)
    markup.add(chipper,card)
    markup.add(mm)
    return markup


    

from telebot import*
from telebot.types import*
import datetime, time
import payments as c
from config import bot_token, m
import psycopg2

    
from telebot.apihelper import ApiTelegramException
bot_token = bot_token

bot = telebot.TeleBot(bot_token)
#DATABASE CONNECT
DATABASE_URL = "postgresql://postgres:AVCBSt77mxYBNR9lzV46@containers-us-west-106.railway.app:7268/railway"
def connect_to_db():
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    return conn
#FETCH TYPE
def creat():
    conn = connect_to_db()
    cursor = conn.cursor()
    create_table = """CREATE TABLE IF NOT EXISTS UFM_USERS (
    user_id BIGINT NOT NULL,
    user_info varchar(50) NOT NULL,
    join_date varchar(13) NOT NULL,
    type varchar(10) DEFAULT 'VIP',
    PRIMARY KEY(user_id)
    )"""
    cursor.execute(create_table)
    conn.commit()
    cursor.close()
    conn.close()
    
conn = connect_to_db()
cursor = conn.cursor()
    
def create_tips():
    conn = connect_to_db()
    cursor = conn.cursor()
    create_free = "CREATE TABLE IF NOT EXISTS free_tips (tips_date varchar(13) NOT NULL,free_tips TEXT,PRIMARY KEY(tips_date))"
    cursor.execute(create_free)
    conn.commit()
    cursor.close()
    conn.close()
    
def create_oders():
    conn = connect_to_db()
    cursor = conn.cursor()
    create_orders = "CREATE TABLE IF NOT EXISTS orders (date varchar(13) NOT NULL,user_id BIGINT,order_no TEXT NOT NULL,order_type varchar(10) DEFAULT 'VIP',PRIMARY KEY(date,user_id))"
    cursor.execute(create_orders)
    conn.commit()
    cursor.close()
    conn.close()
    
def create_tickets():
    conn = connect_to_db()
    cursor = conn.cursor()
    create_tickets = "CREATE TABLE IF NOT EXISTS tickets (date varchar(13) NOT NULL,ticket_url TEXT NOT NULL,ticket_type varchar(10) DEFAULT 'VIP',PRIMARY KEY(date))"
    cursor.execute(create_tickets)
    conn.commit()
    cursor.close()
    conn.close()

def insert_tips(free_tips,tips_date):
    conn = connect_to_db()
    cursor = conn.cursor()
    query = "INSERT INTO free_tips (free_tips,tips_date) VALUES (%s,%s)"
    cursor.execute(query, (free_tips,tips_date))
    conn.commit()
    cursor.close()
    conn.close()

def insert_user_data(user_id, join_date, user_info):
    conn = connect_to_db()
    cursor = conn.cursor()
    query = "INSERT INTO UFM_USERS (user_id, join_date, user_info) VALUES (%s, %s, %s) ON CONFLICT (user_id) DO NOTHING;"
    cursor.execute(query, (user_id, join_date, user_info))
    conn.commit()
    cursor.close()
    conn.close()
    
def insert_tiket(date,ticket_url,ticket_type):
    conn = connect_to_db()
    cursor = conn.cursor()
    query = "INSERT INTO tickes (date, ticket_url, ticket_type) VALUES (%s, %s, %s) ON CONFLICT (date) DO NOTHING;"
    cursor.execute(query, (date,ticket_url,ticket_type))
    conn.commit()
    cursor.close()
    conn.close()


user_dict = {}
class User:
    def __init__(self, name):
        self.name = name
        self.number = None

def is_subscribed(chat_id, user_id):
    try:
        creat()
        response = bot.get_chat_member(chat_id, user_id)
        if response.status == 'left':
            return False
        else:
            return True
    except ApiTelegramException as e:
        if e.result_json['description'] == 'Bad Request: chat not found':
            return False

#BUTTONS
def vipreply_btn():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2,one_time_keyboard=True)
    cs = types.KeyboardButton(text="CORRECT SCORE",)
    ht_ft = types.KeyboardButton(text="HT/FT",)
    markup.add(cs,ht_ft)
    return markup

def main_btn():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    vip = types.KeyboardButton(text="💰VIP GAMES💰",)
    account = types.KeyboardButton(text="👤My account",)
    freetips = types.KeyboardButton(text="⛑️Free tips",)
    orders = types.KeyboardButton(text="🧾My orders",)
    support = types.KeyboardButton(text="🧑‍💻Admin",)
    others = types.KeyboardButton(text="❌Close this menue",)
    markup.add(vip)
    markup.add(account,freetips)
    markup.add(orders,support)
    markup.add(others)
    return markup
def yesorno_btn():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2,one_time_keyboard=True)
    no = types.KeyboardButton(text="No",)
    yes = types.KeyboardButton(text="Yes",)
    markup.add(yes,no)
    return markup
#PAYMENTS
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
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
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

def mm_sim():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    mtn = types.KeyboardButton(text="MTN",)
    Airtel = types.KeyboardButton(text="AIRTEL",)
    markup.add(mtn,Airtel)
    return markup

def chipper_btn():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("CHIPPER CASH PAY", url=f"{m.chippercash}"))
    return markup


#OTHERS
def sub():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("JOIN CHANNEL 📢", url=f"https://t.me/{m.main_channel}"))
    return markup

def commands_btn():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("MAIN MENU 🔰", callback_data="menu"))
    return markup

def start_btn():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("FREE TIPS ⛑️", callback_data="free"),
               InlineKeyboardButton("VIP MATCHES 💯", callback_data="vip-menu"))
    return markup

def help_btn():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("MAIN MENU 🔰", callback_data="menu"),
               InlineKeyboardButton("CONTINUE ➡️", callback_data="vip-menu"))
    return markup

def free_btn():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("BACK 🔙", callback_data="menu"),
               InlineKeyboardButton("TODAYS TIPS ⛑️", callback_data="today's_tips"))
    return markup

def today_tips_btn():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("MAIN MENU 🔰", callback_data="menu"),)
    #put reply keyboard (generate booking kode)
    return markup

def freetips_btn():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(
               InlineKeyboardButton("💯 SURE ODDS", callback_data="vip-menu"))
    return markup
def reload_btn():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("BACK 🔙", callback_data="menu"),
               InlineKeyboardButton("💯 SURE ODDS", callback_data="vip-menu"))
    return markup
#VIP-SECTION
def vipmenu_btn():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("TODAY'S GAMES ✅", callback_data="vip"),
               InlineKeyboardButton("HOW IT WORKS ⁉️", callback_data="how"))
    return markup

def how_btn():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("JOIN VIP NOW 💰", callback_data="vip-menu"),
               InlineKeyboardButton("ASK MORE 🤵", callback_data="admin"))
    return markup
#reply keyboard for admin
def admin_btn():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("ADMIN 🕴️", url='https://t.me/talktotegs'))
    return markup

def vip_btn():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("CORRECT SCORE", callback_data="cs"),
               InlineKeyboardButton("HT/FT", callback_data="ht/ft_menu"))
    return markup

def htft_btn():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("BACK 🔙", callback_data="vip"))
    return markup

def cs_btn():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("BUY MATCHES NOW 💰", callback_data="subscribe"))
    markup.add(InlineKeyboardButton("BACK 🔙", callback_data="vip"),
               InlineKeyboardButton("MAIN MENU 🔰", callback_data="menu"))
    
    return markup

#REPLY KEYBOARD FOR COUNTRIES
def country_btn():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("UGANDA 🇺🇬", callback_data="ug"),
               InlineKeyboardButton("KENYA 🇰🇪", callback_data="ke"),
               InlineKeyboardButton("GHANA 🇬🇭", callback_data="gh"),
               InlineKeyboardButton("RWANDA 🇷🇼", callback_data="rw"),
               InlineKeyboardButton("TANZANIA 🇹🇿", callback_data="tz"),
               InlineKeyboardButton("USA 🇵🇷", callback_data="usa"),
               InlineKeyboardButton("NIGERIA 🇳🇬", callback_data="ni"))
    markup.add(InlineKeyboardButton("🔙", callback_data="cs"), 
               InlineKeyboardButton("OTHERS 🌐", callback_data="others"))
    return markup


def ug_btn():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("JOIN VIP", callback_data="ug_vip"),
               InlineKeyboardButton("JOIN VVIP", callback_data="ug_vvip"))
    markup.add(InlineKeyboardButton("NOT SURE ⁉️", callback_data="vip_des"))
    return markup
def ke_btn():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("JOIN VIP", callback_data="ke_vip"),
               InlineKeyboardButton("JOIN VVIP", callback_data="ke_vvip"))
    markup.add(InlineKeyboardButton("NOT SURE ⁉️", callback_data="vip_des"))
    return markup
def gh_btn():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("JOIN VIP", callback_data="gh_vip"),
               InlineKeyboardButton("JOIN VVIP", callback_data="gh_vvip"))
    markup.add(InlineKeyboardButton("NOT SURE ⁉️", callback_data="vip_des"))
    return markup
def rw_btn():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("JOIN VIP", callback_data="rw_vip"),
               InlineKeyboardButton("JOIN VVIP", callback_data="rw_vvip"))
    markup.add(InlineKeyboardButton("NOT SURE ⁉️", callback_data="vip_des"))
    return markup
def tz_btn():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("JOIN VIP", callback_data="tz_vip"),
               InlineKeyboardButton("JOIN VVIP", callback_data="tz_vvip"))
    markup.add(InlineKeyboardButton("NOT SURE ⁉️", callback_data="vip_des"))
    return markup
def usa_btn():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("JOIN VIP", callback_data="usa_vip"),
               InlineKeyboardButton("JOIN VVIP", callback_data="usa_vvip"))
    markup.add(InlineKeyboardButton("NOT SURE ⁉️", callback_data="vip_des"))
    return markup
def ng_btn():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("JOIN VIP", callback_data="ng_vip"),
               InlineKeyboardButton("JOIN VVIP", callback_data="ng_vvip"))
    markup.add(InlineKeyboardButton("NOT SURE ⁉️", callback_data="vip_des"))
    return markup
def others_btn():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("BACK 🔙", callback_data="country"),
               InlineKeyboardButton("TALK TO ADMIN", callback_data="admin"))
    markup.add(InlineKeyboardButton("NOT SURE ⁉️", callback_data="vip_des"))
    return markup


def vipdes_btn():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("BACK 🔙", callback_data="country"))
    return markup

#MODE OF PAYMENTS



#CALLBACK
@bot.callback_query_handler(func=lambda call: True)
def callback_data(call):
    if call.message:
        price_tag = "PRICE IS"
        #FREE TIPS
        if call.data == "free":
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text=m.freetips_msg, reply_markup=free_btn(),
                                  parse_mode = "Markdown")
        elif call.data == "today's_tips":
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text=m.free_msg1, reply_markup=freetips_btn(),
                                  parse_mode = "Markdown")
        elif call.data == "reload":
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text= "Updated \n" + m.free_msg, reply_markup=reload_btn(),
                                  parse_mode = "Markdown")
       #MAIN MENU     
        elif call.data == "menu":
     
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text=m.startmsg, reply_markup=start_btn(),
                                  parse_mode = "Markdown", 
                                   disable_web_page_preview=True)
        #VIP SECTION
        elif call.data == "vip-menu":
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text=m.vipmenu_msg, reply_markup=vipmenu_btn(),
                                 parse_mode = "Markdown")
        elif call.data == "vip":
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text=m.vip_msg, reply_markup=vip_btn(),
                                 parse_mode = "Markdown")
        elif call.data == "how":
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text=m.how_msg, reply_markup=how_btn(),
                                 parse_mode = "Markdown")
        
        elif call.data == "cs":
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text=m.cs_msg, reply_markup=cs_btn(),
                                  parse_mode = "Markdown")
        elif call.data == "subscribe":
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text=m.country_msg, reply_markup=country_btn(),
                                 parse_mode = "Markdown")
        elif call.data == "country":
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text=m.country_msg, reply_markup=country_btn(),
                                  parse_mode = "Markdown")
        #COUNTRY SECTION    
        elif call.data == "ug":
            ug = 47000
            ug_msg = f"*VIP @;* {ug}ugx | *VVIP @;* {30*ug}ugx"
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text=ug_msg, reply_markup=ug_btn(),
                                  parse_mode = "Markdown")
        elif call.data == "ke":
            ke = 1535
            ke_msg = f"*VIP @;* {ke}kes | *VVIP @;* {30*ke}kes"
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text=ke_msg, reply_markup=ke_btn(),
                                  parse_mode = "Markdown")
        elif call.data == "gh":
            gh = 99.3
            gh_msg = f"*VIP @;* {gh}cedi | *VVIP @;* {30*gh}cedi"
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text=gh_msg, reply_markup=gh_btn(),
                                  parse_mode = "Markdown")
        elif call.data == "rw":
            rw = 13370
            rw_msg = f"*VIP @;* {rw}rwf | *VVIP @;* {30*rw}rwf"
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text=rw_msg, reply_markup=rw_btn(),
                                  parse_mode = "Markdown")
        elif call.data == "tz":
            tz = 30492
            tz_msg = f"*VIP @;* {tz}tzs | *VVIP @;* {30*tz}tzs"
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text=tz_msg, reply_markup=tz_btn(),
                                  parse_mode = "Markdown")
        elif call.data == "usa":
            usa = 17.473
            usa_msg = f"*VIP @;* {usa}$ | *VVIP @;* {30*usa}$"
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text=usa_msg, reply_markup=usa_btn(),
                                  parse_mode = "Markdown")
        elif call.data == "ng":
            ng = 6500
            ng_msg = f"*VIP @;* {ng}ngn | *VVIP @;* {30*ng}ngn"
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text=ng_msg, reply_markup=ng_btn(),
                                  parse_mode = "Markdown")
            
        elif call.data == "vip_des":
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text=m.vipdes_msg, reply_markup=vipdes_btn(),
                                  parse_mode = "Markdown")
        #PAYMENTS
        elif call.data == "ug_vip":
            text="*Select your mode of payment*"
            ugvip_msg = "UGANDA VIP PAYMENT"
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text=ugvip_msg,
                                  parse_mode = "Markdown")
            bot.send_message(call.message.chat.id, text=text
                         , reply_markup=ugvip_btn(),parse_mode = "Markdown")
        elif call.data == "ke_vip":
            text="*Select your mode of payment*"
            ugvip_msg = "KENYA VIP PAYMENT"
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text=ugvip_msg,
                                  parse_mode = "Markdown")
            bot.send_message(call.message.chat.id, text=text
                         , reply_markup=kevip_btn(),parse_mode = "Markdown")
        elif call.data == "gh_vip":
            text="*Select your mode of payment*"
            ugvip_msg = "GHANA VIP PAYMENT"
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text=ugvip_msg,
                                  parse_mode = "Markdown")
            bot.send_message(call.message.chat.id, text=text
                         , reply_markup=ghvip_btn(),parse_mode = "Markdown")
        elif call.data == "rw_vip":
            text="*Select your mode of payment*"
            ugvip_msg = "RWANDA VIP PAYMENT"
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text=ugvip_msg,
                                  parse_mode = "Markdown")
            bot.send_message(call.message.chat.id, text=text
                         , reply_markup=rwvip_btn(),parse_mode = "Markdown")
        elif call.data == "tz_vip":
            text="*Select your mode of payment*"
            ugvip_msg = "TANZANIA VIP PAYMENT"
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text=ugvip_msg,
                                  parse_mode = "Markdown")
            bot.send_message(call.message.chat.id, text=text
                         , reply_markup=tzvip_btn(),parse_mode = "Markdown")
        elif call.data == "usa_vip":
            text="*Select your mode of payment*"
            ugvip_msg = "USA VIP PAYMENT"
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text=ugvip_msg,
                                  parse_mode = "Markdown")
            bot.send_message(call.message.chat.id, text=text
                         , reply_markup=usavip_btn(),parse_mode = "Markdown")
        elif call.data == "ni_vip":
            text="*Select your mode of payment*"
            ugvip_msg = "RWANDA VIP PAYMENT"
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text=ugvip_msg,
                                  parse_mode = "Markdown")
            bot.send_message(call.message.chat.id, text=text
                         , reply_markup=nivip_btn(),parse_mode = "Markdown")

            

#COMMANDS



@bot.message_handler(commands=['start'])
def send_welcome(message):
    create_tips()
    if not is_subscribed(m.CHAT_ID,message.chat.id):
        # user is not subscribed. send message to the user
        bot.send_message(message.chat.id, text=m.not_sub_msg
                         , reply_markup=sub(),parse_mode = "Markdown")
    else:
        create_oders()
        user_id = message.from_user.id
        user_name = message.from_user.first_name
        messageTime = message.date
        messageTime = datetime.datetime.utcfromtimestamp(messageTime) # datetime format
        messageTime = messageTime.strftime('%d/%m/%Y') # formatted datetime
        join_date = str(messageTime)
        user_info = f"{message.from_user.first_name} {message.from_user.last_name}"
        insert_user_data(user_id, join_date, user_info)
        mention = "["+user_name+"](tg://user?id="+str(user_id)+")"
        bot.send_message(message.chat.id, text=f"**HEY {mention}**" + m.startmsg,
                         
                         parse_mode = "Markdown")
        bot.send_message(message.chat.id, text=m.main_msg,reply_markup=main_btn()
                         ,parse_mode = "Markdown")
        
        

@bot.message_handler(commands=['help'])
def send_welcome(message):
    if not is_subscribed(m.CHAT_ID,message.chat.id):
        # user is not subscribed. send message to the user
        bot.send_message(message.chat.id, text=m.not_sub_msg
                         , reply_markup=sub())
    else:
        bot.send_message(message.chat.id, text=m.helpmsg, reply_markup=help_btn())
        
@bot.message_handler(commands=['commands'])
def send_welcome(message):
    if not is_subscribed(m.CHAT_ID,message.chat.id):
        # user is not subscribed. send message to the user
        bot.send_message(message.chat.id, text=m.not_sub_msg
                         , reply_markup=sub())
    else:
        cmdmsg = "The following commands are available: \n"
        for key in m.commands:  # generate help text out of the commands dictionary defined at the top
            cmdmsg += "/" + key + ": "
            cmdmsg += m.commands[key] + "\n"
        bot.send_message(message.chat.id, text=cmdmsg, reply_markup=commands_btn())
        
@bot.message_handler(commands=['free'])
def send_welcome(message):
    messageTime = message.date
    messageTime = datetime.datetime.utcfromtimestamp(messageTime) # datetime format
    messageTime = messageTime.strftime('%d/%m/%Y') # formatted datetime
    current_date = str(messageTime)
    #FETCH DATA
    conn = connect_to_db()
    cursor = conn.cursor()
    postgreSQL_select_Query = "select free_tips from free_tips where tips_date='{}'"
    cursor.execute(postgreSQL_select_Query.format(current_date))
    tip = cursor.fetchone()
    conn.commit()
    #END
    try:
        if not is_subscribed(m.CHAT_ID,message.chat.id):
        # user is not subscribed. send message to the user
            bot.send_message(message.chat.id, text=m.not_sub_msg
                         , reply_markup=sub())
        else:
            bot.send_message(message.chat.id, text=m.free_msg.format(current_date,tip[0]), reply_markup=freetips_btn(),parse_mode = "Markdown")
    except (Exception, psycopg2.DatabaseError) as e:
            bot.send_message(message.chat.id, text=m.no_free_msg.format(current_date),parse_mode = "Markdown")
            print(e)
        
@bot.message_handler(commands=['update'])
def send_welcome(message):
    messageTime = message.date
    messageTime = datetime.datetime.utcfromtimestamp(messageTime) # datetime format
    messageTime = messageTime.strftime('%d/%m/%Y') # formatted datetime
    tips_date = str(messageTime)
    free_tips = message.text.split(None,1)[1]
    user_id = message.from_user.id
    if user_id not in m.admin:
        bot.send_message(message.chat.id, text="⚠️You must be admin to do this")
    else:
        insert_tips(free_tips,tips_date)
        bot.send_message(message.chat.id, text=free_tips,parse_mode = "Markdown")
        
@bot.message_handler(commands=['delete'])
def send_welcome(message):
    messageTime = message.date
    messageTime = datetime.datetime.utcfromtimestamp(messageTime)
    messageTime = messageTime.strftime('%d/%m/%Y') # formatted datetime
    tips_date = str(messageTime)
    user = message.from_user.id
    text="Tip for DATE: {} successfully ✅"
    current_date = message.text.split(None,1)[1]
    if user not in m.admin:
        bot.send_message(message.chat.id, text="⚠️You must be admin to do this")
    else:
        try:
            conn = connect_to_db()
            cursor = conn.cursor()
            cursor.execute(f"DELETE FROM free_tips WHERE tips_date = '{current_date}'")
            conn.commit()
            conn.close()
            bot.send_message(message.chat.id, text=text.format(current_date))
        except (Exception, psycopg2.DatabaseError) as e:
            bot.reply_to(message, text=f"Make sure your date is well formated as {current_date}")
            print(e)
       
@bot.message_handler(commands=['admin'])
def send_welcome(message):
    if not is_subscribed(m.CHAT_ID,message.chat.id):
        # user is not subscribed. send message to the user
        bot.send_message(message.chat.id, text=m.not_sub_msg
                         , reply_markup=sub())
    else:
        #USAGES    
        user_id = message.from_user.id    
        user_name = message.from_user.first_name
        
        mention = "["+user_name+"](tg://user?id="+str(user_id)+")" 
            #END USAGES    
        bot.send_message(message.chat.id,text=m.admin_msg.format(mention,user_id), 
                             reply_markup=admin_btn(),parse_mode = "Markdown",
                             disable_web_page_preview=True)
  
@bot.message_handler(commands=['confirm'])
def confirm_client (message):
    user_id = message.text.split()[1]
    user = message.from_user.id
    text = "Payment confirmed with *Order No:* `{}`."
    order_type = "VIP"
    messageTime = message.date
    messageTime = datetime.datetime.utcfromtimestamp(messageTime) # datetime format
    messageTime = messageTime.strftime('%d/%m/%Y') # formatted datetime
    date = str(messageTime)
    order_no = message.message_id
    admin= "ORDER: Date: {} User: {} No: {} Type: {}"
    not_msg = 'You must be an administrator to do this.'
    photo_msg= '_Sending your receipt 🧾 now.._'
    try:
        if user not in m.admin:
            bot.send_message(message.chat.id,not_msg,parse_mode = "Markdown")
        else:
            query = "INSERT INTO orders (date,user_id,order_type,order_no) VALUES (%s,%s,%s,%s)"
            cursor.execute(query,(date,user_id,order_type,order_no))
            conn.commit()
            bot.send_message(message.chat.id,text=admin.format(date,user_id,order_no,order_type),parse_mode = "Markdown")
            bot.send_message(user_id,text=text.format(order_no),parse_mode = "Markdown")
            bot.send_message(user_id,text=photo_msg,parse_mode = "Markdown")
            bot.send_chat_action(user_id, 'upload_photo')  # show the bot "typing" (max. 5 secs)
            time.sleep(3)
            bot.send_photo(user_id,m.ticket, caption = f'VIP TICKET | {order_no}')
    except (Exception, psycopg2.DatabaseError) as e:
        print(e)
        msg = '*User:* {} already has an order settled for *Date:* {}'
        bot.send_message(message.chat.id, msg.format(user_id,date),parse_mode = "Markdown")
        bot.send_message(user_id, 'You already have a running order for *Date:* {}'.format(date),parse_mode = "Markdown")

@bot.message_handler(commands=['verify'])
def confirm_client (message):
    use = message.text.split()[1]
    not_msg = "*Use format:* /verify `83623808484` <-- your transaction ID in your service provider SMS and it must be only digits."
    confirmed= "_Confirming your payment in *TXN ID:* `{}`, please wait ⏳_"
    try:
        if not use.isdigit():
            bot.send_message(message.chat.id,not_msg,parse_mode = "Markdown")
            return
        else:
            bot.forward_message(m.admin, message.chat.id, message.message_id)
            bot.send_message(message.chat.id,confirmed.format(use),parse_mode = "MarkdownV2")
    except Exception as e:
        print(e)
        bot.reply_to(message, 'Oooops... Something went wrong.')
        
@bot.message_handler(commands=['menu'])
def send_welcome(message):
    if not is_subscribed(m.CHAT_ID,message.chat.id):
        # user is not subscribed. send message to the user
        bot.send_message(message.chat.id, text=m.not_sub_msg
                         , reply_markup=sub())
    else:
        bot.send_message(message.chat.id, text=m.main_msg, reply_markup=main_btn(),parse_mode = "Markdown")

        
@bot.message_handler(commands=['info'])
def info_bot(message):
    text = """
    _Here is your telegram info_
    🧔*ID:* `{}`
    👤*NAME:* {}
    🌐*USERNAME:* {}
    ▫️*LANG:* {}
    ▫️*TYPE:* {} \n_Updated on {}_"""
    text2 = """
    _Here is your telegram info_
    🧔*ID:* `{}`
    👤*NAME:* {}
    🌐*USERNAME:* {}
    ▫️*LANG:* {}
    ▫️*TYPE:* {} \n_Updated on {}_"""
    messageTime = message.date
    messageTime = datetime.datetime.utcfromtimestamp(messageTime) # datetime format
    messageTime = messageTime.strftime('%d/%m/%Y %H:%M:%S') # formatted datetime
    TimeStamp = str(messageTime)
    user_id = message.from_user.id
    uname = message.from_user.username
    unamef = f"@{uname}"
    lang = message.from_user.language_code
    premium = message.from_user.is_premium
    name = message.from_user.first_name
    name2 = message.from_user.last_name
    namet = "["+name+"](tg://user?id="+str(user_id)+")"
    
    try:
        namet2 = "["+name + name2+"](tg://user?id="+str(user_id)+")"
        bot.send_message(message.chat.id, text=text.format(user_id,namet2,unamef,lang,premium,TimeStamp),parse_mode = "Markdown")
    except Exception as e:
        print(e)
        bot.reply_to(message, text=text.format(user_id,namet,unamef,lang,premium,TimeStamp),parse_mode = "Markdown")
        
@bot.message_handler(commands=['user'])
def send_info(message):
    user = message.forward_from.id
    msg = '*USER:* `{}`'
    bot.send_message(message.chat.id, 
                         msg.format(user),
                         parse_mode = "Markdown")
        
@bot.message_handler(commands=['cast'])
def send_cast(message):
    msg = message.text.split(None,1)[1]
    user = message.from_user.id
    #start
    conn = connect_to_db()
    cursor = conn.cursor()
    db_users = "select user_id from UFM_USERS where type ='ORD'"
    cursor.execute(db_users)
    u = cursor.fetchall()
    users = [row[0] for row in u]
    conn.commit()
    #fetch users
    jip = '997667609'
    try:
        if user not in m.admin:
           bot.send_message(message.chat.id,text=f"You require admin permission to do this ‼️",parse_mode = "Markdown")
        else:
            #bot.send_message(message.chat.id,f'_These are your users_\n{users}',parse_mode = "Markdown")
            bot.send_message(chat_id=jip,text=msg,parse_mode = "Markdown")
    except Exception as e:
        bot.send_message(message.chat.id, 
                         f'*Oooops... Something went wrong.*\n`These are your users`\n{users}',
                         parse_mode = "Markdown")   
    

@bot.message_handler(commands=['reload'])
def send_welcome(message):
    if not is_subscribed(m.CHAT_ID,message.chat.id):
        # user is not subscribed. send message to the user
        bot.send_message(message.chat.id, text=m.not_sub_msg
                         , reply_markup=sub())
    else:
        bot.send_message(message.chat.id, text="_Bot Reloaded_",parse_mode = "Markdown")
        bot.send_message(message.chat.id, text=m.main_msg, reply_markup=main_btn(),parse_mode = "Markdown")
        
@bot.message_handler() 
def get_message(message):
    create_tickets()
    if not is_subscribed(m.CHAT_ID,message.chat.id):
        # user is not subscribed. send message to the user
        bot.send_message(message.chat.id, text=m.not_sub_msg
                         , reply_markup=sub())
    else:
        if message.text == "💰VIP GAMES💰":
            bot.send_message(message.chat.id,
                                  text=m.vip_msg, reply_markup=vipreply_btn(),parse_mode = "Markdown")
        elif message.text == "👤My account":
            try:
                messageTime = message.date
                messageTime = datetime.datetime.utcfromtimestamp(messageTime) # datetime format
                messageTime = messageTime.strftime('%d/%m/%Y')
                TimeStamp = str(messageTime)
                name2 = message.from_user.last_name
                name = message.from_user.first_name
                user_id = message.from_user.id
                #FETCH DATA
                conn = connect_to_db()
                cursor = conn.cursor()
                postgreSQL_select_Query = f"select type from UFM_USERS where user_id='{user_id}'"
                cursor.execute(postgreSQL_select_Query)
                type = cursor.fetchone()
                conn.commit()
                query = "select order_no from orders where user_id='{}' and date = '{}'"
                cursor.execute(query.format(user_id,TimeStamp))
                order = cursor.fetchone()
                conn.commit()
                #END
                mention = "["+name+"](tg://user?id="+str(user_id)+")"
                acc = f"📊 Your account information.\n\n🧔*USER/N0:* `{user_id}`\n▫️*NAME:* {mention} \n▫️*ACC/TYPE:* {type[0]} \n💰*ORDERS:* `{order[0]}` | _{TimeStamp}_\n\n_Date: {TimeStamp}_"
                bot.send_message(message.chat.id,
                                  text=acc,parse_mode = "Markdown",
                         disable_web_page_preview=True
                         )
            except (Exception, psycopg2.DatabaseError) as e:
                acc = f"📊 Your account information.\n\n🧔*USER/N0:* `{user_id}`\n▫️*NAME:* {mention} \n▫️*ACC/TYPE:* {type[0]} \n💰*ORDERS:* `No oder yet`\n\n_Date: {TimeStamp}_"
                bot.send_message(message.chat.id,
                                  text=acc,parse_mode = "Markdown",
                         disable_web_page_preview=True,
                         )
                print(e)
                
        elif message.text == "⛑️Free tips":
            bot.send_message(message.chat.id,
                                  text=m.freetips_msg, reply_markup=free_btn())
        elif message.text == "🧾My orders":
            orders_msg = "These are your oders.\n\nACTIVE ORDER: {}\nplaced on {}"
            user= message.from_user.id
            #time
            messageTime = message.date
            messageTime = datetime.datetime.utcfromtimestamp(messageTime) # datetime format
            messageTime = messageTime.strftime('%d/%m/%Y') # formatted datetime
            date = str(messageTime)
            #connect
            conn = connect_to_db()
            cursor = conn.cursor()
            query = "select order_no from orders where user_id='{}' and date = '{}'"
            cursor.execute(query.format(user,date))
            order = cursor.fetchone()
            conn.commit()
            #fetch end
            try:
                bot.send_message(message.chat.id,
                                  text=orders_msg.format(order[0],date),parse_mode = "Markdown")    
            except (Exception, psycopg2.DatabaseError) as e:
                bot.send_message(message.chat.id, text=f"You have no order for today `{date}`",parse_mode = "Markdown")
                print(e)
                
                
        elif message.text == "❌Close this menue":
            mainmsg = "PROCEED WITH THIS MENU NOW"
            bot.send_message(message.chat.id,
                                  text="▫️Key-buttons removed.. Re-enable with /menu", reply_markup=ReplyKeyboardRemove())
            bot.send_message(message.chat.id,
                                  text=mainmsg, reply_markup=start_btn(), parse_mode = "Markdown")
        elif message.text == "🧑‍💻Admin":
            support_msg = "Summerise your problem and it will be forwarded to the admin directly for answering.\n Thanks.."
            msg = bot.send_message(message.chat.id,
                                  text=support_msg,reply_markup=ReplyKeyboardRemove())
            bot.register_next_step_handler(msg, process_problem_step)
        elif message.text == "Mobile Money":
            mm_msg = "*WHAT SIMCARD (🇺🇬) DO YOU USE*"
            bot.send_message(message.chat.id,text=mm_msg,reply_markup=mm_sim(),parse_mode = "Markdown")
        elif message.text == "MTN":
            mtn_msg = "*Send me the MTN number you're going to transact with.*"
            msg = bot.send_message(message.chat.id,
                                   text=mtn_msg,reply_markup=ReplyKeyboardRemove(),
                                   parse_mode = "Markdown")
            bot.register_next_step_handler(msg, mtnnumber_step)
        elif message.text == "AIRTEL":
            mtn_msg = "*Send me the Airtel number you're going to transact with.*"
            msg = bot.send_message(message.chat.id,text=mtn_msg,parse_mode = "Markdown",reply_markup=ReplyKeyboardRemove())
            bot.register_next_step_handler(msg, airtelnumber_step)
        elif message.text == "Chipper Cash":
            link = "https://chippercash.com"
            text = "CHIPPER-CHASH SITE"
            chipper_msg = """⚠️Please register and verify your chipper-Cash account with an appropriate legal document at [{}]({}).\n*Already registered?*, follow the payment link below to pay for today's *VIP games*.
            """
            bot.send_message(message.chat.id,text=chipper_msg.format(text,link),reply_markup=chipper_btn(),disable_web_page_preview=True,parse_mode = "Markdown")
        elif message.text == "MTN mpesa":
            MTN= "0773936516"
            text= "*Dail* `*156#` then east Africa..."
            bot.send_message(message.chat.id,text=text,parse_mode = "Markdown")
        elif message.text == "Card 💳":
            text= "Will be available soon 🙂"
            bot.send_message(message.chat.id,text=text)
            
        elif message.text == "CORRECT SCORE":
            bot.send_message(chat_id=message.chat.id,
                                  text=m.cs_msg, reply_markup=cs_btn(),
                                  parse_mode = "Markdown")
        elif message.text == "HT/FT":
            msg = "*🔘HT/FT MENU*\n\n_⚠️No HT/FT matches today.\nPlease proceed with CORRECT SCORE matches._"
            bot.send_message(chat_id=message.chat.id,
                                  text=msg,
                                  parse_mode = "Markdown")
            bot.send_message(message.chat.id, text=m.main_msg,reply_markup=main_btn()
                         ,parse_mode = "Markdown")
        elif message.text == "Admin":
            msg = f"*CONTACT ADMIN HERE*\n\n⚠️Contact admin here for payment issues only. Click on UFM ADMIN below 👇.\n*🧑‍💻ADMIN:* [UFM ADMIN]({m.admin_direct})\n\n_All rights reserved._"
            bot.send_message(message.chat.id, text=msg,reply_markup=main_btn(),disable_web_page_preview=True
                         ,parse_mode = "Markdown")
        
            
            
            

def mtnnumber_step(message):
    try:
        chat_id = message.chat.id
        number = message.text
        mtn = "0773936516"
        amount = 47000
        if not number.isdigit():
            msg = bot.reply_to(message, f"⚠️({number}) should only be 'numbers' and 10 digits.\n*Send me the Airtel number you're going to transact with.*",parse_mode = "Markdown")
            bot.register_next_step_handler(msg, mtnnumber_step)
            return
        user = User(number)
        user_dict[chat_id] = user
        no_msg = """*Use* mobile number `{}` to send `{}` ugx to `{}`\n*Or*\n*Dail* `*185*1*{}*{}#` *then input your pin.*\n*After* wait for verification or use /verify "your transaction id" or send a screenshot of the payment.\n\n_All rights reserved._
        """
        user.number = number
        bot.send_message(chat_id,text=no_msg.format(user.number,amount,mtn,mtn,amount),parse_mode = "Markdown")
    except Exception as e:
        print(e)
        bot.send_message(message, '⚠️Oooops... Something went wrong.')
        
def airtelnumber_step(message):
    try:
        chat_id = message.chat.id
        number = message.text
        airtel = "0708527456"
        amount = "47000"
        if not number.isdigit():
            msg = bot.reply_to(message, "⚠️(SIM NUMBER) should be only 'numbers' and 10 digits.\n*Send me the Airtel number you're going to transact with.*",parse_mode = "Markdown")
            bot.register_next_step_handler(msg, airtelnumber_step)
            return
        user = User(number)
        user_dict[chat_id] = user
        no_msg = """*Use* mobile number `{}` to send `{}` ugx to `{}`\n*Or*\n*Dail* `*185*1*{}*{}#` *then input your pin.*\n*After* wait for verification or use /verify "your transaction id" or send a screenshot of the payment.\n\n_All rights reserved._
        """
        user.number = number
        bot.send_message(chat_id,text=no_msg.format(user.number,amount,airtel,airtel,amount),parse_mode = "Markdown")
    except Exception as e:
        print(e)
        bot.reply_to(message, '⚠️Oooops... Something went wrong.')

      
def process_problem_step(message):
    try:
        chat_id = message.chat.id
        user_name = message.from_user.first_name
        user_id = message.from_user.id
        name = message.text
        user = User(name)
        mention = "["+user_name+"](tg://user?id="+str(user_id)+")"
        user_dict[chat_id] = user
        msg = bot.send_message(chat_id, text=f'🧔{mention}\n▫️informing... \n_{user.name}_\n\n*‼️Confirm that the above info is what you wanted to ask?👇*',
                         parse_mode = "Markdown",
                         reply_markup=yesorno_btn(),
                         disable_web_page_preview=True)
        bot.forward_message(m.admin, message.chat.id, message.message_id)
        bot.register_next_step_handler(msg, process_menu_step)
        
    except Exception as e:
        print(e)
        bot.reply_to(message, 'Oooops... Something went wrong.')

def process_menu_step(message):
    name = message.text
    user = user_dict[message.chat.id]
    try:
        if message.text == "Yes":
            bot.send_message(message.chat.id, text=f'*Fowarded successfully...*',
                               parse_mode = "Markdown",
                               reply_markup=main_btn())  
        elif message.text == "No":
             msg = bot.send_message(message.chat.id, text='*Retype your problem*',
                         parse_mode = "Markdown",
                         disable_web_page_preview=True)
             bot.register_next_step_handler(msg, process_problem_step)           
    except Exception as e:
        print(e)
        bot.send_message(message, 'Oooops... Something went wrong.')




    
        
        
# Enable saving next step handlers to file "./.handlers-saves/step.save".
# Delay=2 means that after any change in next step handlers (e.g. calling register_next_step_handler())
# saving will hapen after delay 2 seconds.
bot.enable_save_next_step_handlers(delay=1)

# Load next_step_handlers from save file (default "./.handlers-saves/step.save")
# WARNING It will work only if enable_save_next_step_handlers was called!
bot.load_next_step_handlers()
        
print('BOT IS STARTED SUCCESSFULLY')
bot.infinity_polling()

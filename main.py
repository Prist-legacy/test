from telebot import*
from telebot.types import*
from config import bot_token, m

    
from telebot.apihelper import ApiTelegramException
bot_token = bot_token

bot = telebot.TeleBot(bot_token)


user_dict = {}


class User:
    def __init__(self, name):
        self.name = name
        self.sex = None





def is_subscribed(chat_id, user_id):
    try:
        response = bot.get_chat_member(chat_id, user_id)
        if response.status == 'left':
            return False
        else:
            return True

    except ApiTelegramException as e:
        if e.result_json['description'] == 'Bad Request: chat not found':
            return False

#BUTTONS
def main_btn():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    vip = types.KeyboardButton(text="VIP GAMES",)
    account = types.KeyboardButton(text="My account",)
    freetips = types.KeyboardButton(text="Free tips",)
    orders = types.KeyboardButton(text="My orders",)
    support = types.KeyboardButton(text="support",)
    others = types.KeyboardButton(text="others",)
    markup.add(vip)
    markup.add(account,freetips)
    markup.add(orders,support)
    markup.add(others)
    return markup


def sub():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("JOIN CHANNEL 📢", url="https://t.me/pristbank"))
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
    markup.add(InlineKeyboardButton("RELOAD TIP 🔃", callback_data="reload"),
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
    markup.add(InlineKeyboardButton("ADMIN 🕴️", url='https://t.me/pristlegacy'))
    markup.add(InlineKeyboardButton("MAIN MENU 🔰", callback_data="menu"))
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
    markup.add(InlineKeyboardButton("JOIN VIP", callback_data="join_vip"),
               InlineKeyboardButton("JOIN VVIP", callback_data="join_vvip"))
    markup.add(InlineKeyboardButton("NOT SURE ⁉️", callback_data="vip_des"))
    return markup
def ke_btn():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("JOIN VIP", callback_data="join_vip"),
               InlineKeyboardButton("JOIN VVIP", callback_data="join_vvip"))
    markup.add(InlineKeyboardButton("NOT SURE ⁉️", callback_data="vip_des"))
    return markup
def gh_btn():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("JOIN VIP", callback_data="join_vip"),
               InlineKeyboardButton("JOIN VVIP", callback_data="join_vvip"))
    markup.add(InlineKeyboardButton("NOT SURE ⁉️", callback_data="vip_des"))
    return markup
def rw_btn():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("JOIN VIP", callback_data="join_vip"),
               InlineKeyboardButton("JOIN VVIP", callback_data="join_vvip"))
    markup.add(InlineKeyboardButton("NOT SURE ⁉️", callback_data="vip_des"))
    return markup
def tz_btn():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("JOIN VIP", callback_data="join_vip"),
               InlineKeyboardButton("JOIN VVIP", callback_data="join_vvip"))
    markup.add(InlineKeyboardButton("NOT SURE ⁉️", callback_data="vip_des"))
    return markup
def usa_btn():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("JOIN VIP", callback_data="join_vip"),
               InlineKeyboardButton("JOIN VVIP", callback_data="join_vvip"))
    markup.add(InlineKeyboardButton("NOT SURE ⁉️", callback_data="vip_des"))
    return markup
def ng_btn():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("JOIN VIP", callback_data="join_vip"),
               InlineKeyboardButton("JOIN VVIP", callback_data="join_vvip"))
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
                                  text="FREE MATCHES MENU", reply_markup=free_btn())
        elif call.data == "today's_tips":
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text=m.freetips_msg, reply_markup=freetips_btn())
        elif call.data == "reload":
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text= "Updated \n" + m.freetips_msg, reply_markup=reload_btn())
       #MAIN MENU     
        elif call.data == "menu":
     
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text=m.startmsg, reply_markup=start_btn(), 
                                   disable_web_page_preview=True)
        #VIP SECTION
        elif call.data == "vip-menu":
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text=m.vipmenu_msg, reply_markup=vipmenu_btn())
        elif call.data == "vip":
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text=m.vip_msg, reply_markup=vip_btn())
        elif call.data == "how":
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text=m.how_msg, reply_markup=how_btn())
        
        elif call.data == "cs":
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text=m.cs_msg, reply_markup=cs_btn())
        elif call.data == "subscribe":
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text=m.country_msg, reply_markup=country_btn())
        elif call.data == "country":
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text=m.country_msg, reply_markup=country_btn())
        #COUNTRY SECTION    
        elif call.data == "ug":
            ug = 47000
            ug_msg = f"VIP PRICE; {ug}ugx \nVVIP PRICE; {ug}ugx"
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text=ug_msg, reply_markup=ug_btn())
        elif call.data == "ke":
            ke = 1535
            ke_msg = f"VIP PRICE; {ke}kes \nVVIP PRICE; {ke}kes"
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text=ke_msg, reply_markup=ke_btn())
        elif call.data == "gh":
            gh = 99.3
            gh_msg = f"VIP PRICE; {gh}cedi \nVVIP PRICE; {gh}cedi"
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text=gh_msg, reply_markup=gh_btn())
        elif call.data == "rw":
            rw = 13370
            rw_msg = f"VIP PRICE; {rw}rwf \nVVIP PRICE; {rw}rwf"
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text=rw_msg, reply_markup=rw_btn())
        elif call.data == "tz":
            tz = 30492
            tz_msg = f"VIP PRICE; {tz}tzs \nVVIP PRICE; {tz}tzs"
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text=tz_msg, reply_markup=tz_btn())
        elif call.data == "usa":
            usa = 17.473
            usa_msg = f"VIP PRICE; {usa}$ \nVVIP PRICE; {usa}$"
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text=usa_msg, reply_markup=usa_btn())
        elif call.data == "ng":
            ng = 6500
            ng_msg = f"VIP PRICE; {ng}ngn \nVVIP PRICE; {ng}ngn"
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text=ng_msg, reply_markup=ng_btn())
            
        elif call.data == "vip_des":
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text=m.vipdes_msg, reply_markup=vipdes_btn())
            

#COMMANDS



@bot.message_handler(commands=['start'])
def send_welcome(message):
    
    if not is_subscribed(m.CHAT_ID,message.chat.id):
        # user is not subscribed. send message to the user
        bot.send_message(message.chat.id, text=m.not_sub_msg
                         , reply_markup=sub())
    else:
        user_id = message.from_user.id
        user_name = message.from_user.first_name
   
        mention = "["+user_name+"](tg://user?id="+str(user_id)+")" 
        #mention = f"{user_name + user_name2}"
        bot.send_message(message.chat.id, text=f"**HEY {mention}**" + m.startmsg, reply_markup=main_btn(), parse_mode = "Markdown")
        
        

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
    if not is_subscribed(m.CHAT_ID,message.chat.id):
        # user is not subscribed. send message to the user
        bot.send_message(message.chat.id, text=m.not_sub_msg
                         , reply_markup=sub())
    else:
        bot.send_message(message.chat.id, text=m.freetips_msg, reply_markup=freetips_btn())
        
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
        bot.send_message(message.chat.id, text=f"USER = {mention}\n" + f"ID = {user_id}\n" + m.admin_msg, 
                             reply_markup=admin_btn(), 
                             parse_mode = "Markdown", 
                             disable_web_page_preview=True)
        

            
    
@bot.message_handler(commands=['reload'])
def send_welcome(message):
    if not is_subscribed(m.CHAT_ID,message.chat.id):
        # user is not subscribed. send message to the user
        bot.send_message(message.chat.id, text=m.not_sub_msg
                         , reply_markup=sub())
    else:
        bot.send_message(message.chat.id, text="Bot Reloaded")
        bot.send_message(message.chat.id, text=m.startmsg, reply_markup=start_btn())
        
@bot.message_handler() 
def get_message(message):
    if message.text == ["admin", "ADMIN", "Admin"]:
        user_id = message.from_user.id
        user_name = message.from_user.first_name
        user_name2 = message.from_user.last_name
        mention = "["+user_name + user_name2+"](tg://user?id="+str(user_id)+")"
        bot.send_chat_action(message.chat.id, 'typing')  # show the bot "typing" (max. 5 secs)
        time.sleep(3)
        bot.send_message(message.chat.id, text=f"USER = {mention}\n" + f"ID = {user_id}\n" + m.admin_msg, 
                             reply_markup=admin_btn(), 
                             parse_mode = "Markdown", 
                             disable_web_page_preview=True)
    elif message.text == "VIP GAMES":
        bot.send_message(message.chat.id,
                                  text=m.vip_msg, reply_markup=vip_btn())
    elif message.text == "My account":
        user_id = message.from_user.id
        user_name2 = message.from_user.last_name
        user_name = message.from_user.first_name
        mention = "["+user_name + user_name2+"](tg://user?id="+str(user_id)+")"
        acc = f"ACCOUNT N0: {user_id}\nTELL NAME: {user_name} \nACCOUNT TYPE: \nORDERS:"
        bot.send_message(message.chat.id,
                                  text=acc, reply_markup=start_btn())
    elif message.text == "Free tips":
        bot.send_message(message.chat.id,
                                  text=m.freetips_msg, reply_markup=free_btn())
    elif message.text == "My orders":
        orders_msg = "These are your oders"
        bot.send_message(message.chat.id,
                                  text=orders_msg)
        
    elif message.text == "Close this menue":
        bot.send_message(message.chat.id,
                                  text="Key-buttons removed", reply_markup=ReplyKeyboardRemove())
        bot.send_message(message.chat.id,
                                  text=m.start_msg, reply_markup=start_btn())
    elif message.text == "support":
        support_msg = "Summerise your problem and it will be forwarded to the admin directly for answering.\n Thanks.."
        msg = bot.send_message(message.chat.id,
                                  text=support_msg)
        bot.register_next_step_handler(msg, process_problem_step)
        
        
def process_problem_step(message):
    try:
        chat_id = message.chat.id
        name = message.text
        user = User(name)
        user_dict[chat_id] = user
        msg = bot.reply_to(message, 'How old are you?')
        bot.register_next_step_handler(msg, process_age_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')
        
def process_sex_step(message):
    try:
        chat_id = message.chat.id
        sex = message.text
        user = user_dict[chat_id]
        if (sex == u'Male') or (sex == u'Female'):
            user.sex = sex
        else:
            raise Exception("Unknown sex")
        bot.send_message(chat_id, 'Nice to meet you ' + user.name + '\n Sex:' + user.sex)
    except Exception as e:
        bot.reply_to(message, 'oooops')
        
        
# Enable saving next step handlers to file "./.handlers-saves/step.save".
# Delay=2 means that after any change in next step handlers (e.g. calling register_next_step_handler())
# saving will hapen after delay 2 seconds.
bot.enable_save_next_step_handlers(delay=1)

# Load next_step_handlers from save file (default "./.handlers-saves/step.save")
# WARNING It will work only if enable_save_next_step_handlers was called!
bot.load_next_step_handlers()
        
print('BOT IS STARTED SUCCESSFULLY')
bot.polling()

# bot.py
import telebot

TOKEN ='7340012892:AAHzzwcyJKdt_kqV2ObarhRMZkbYESBMii4'
bot = telebot.TeleBot(TOKEN)

user_data = {}

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "سلام! لطفاً نام خود را وارد کنید:")
    bot.register_next_step_handler(message, get_name)

def get_name(message):
    user_data['name'] = message.text
    bot.send_message(message.chat.id, "سن خود را وارد کنید:")
    bot.register_next_step_handler(message, get_age)

def get_age(message):
    user_data['age'] = message.text
    bot.send_message(message.chat.id, "شماره تماس خود را وارد کنید:")
    bot.register_next_step_handler(message, save_data)

def save_data(message):
    user_data['phone'] = message.text
    with open("data.csv", "a", encoding="utf-8") as f:
        f.write(f"{user_data['name']},{user_data['age']},{user_data['phone']}\n")
    bot.send_message(message.chat.id, "اطلاعات شما با موفقیت ذخیره شد. ممنونم 🌟")

bot.infinity_polling()
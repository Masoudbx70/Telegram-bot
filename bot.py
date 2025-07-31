import telebot
import os

# توکن رو از متغیر محیطی بخون
TOKEN = os.environ.get("7340012892:AAHzzwcyJKdt_kqV2ObarhRMZkbYESBMii4")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "سلام! به ربات خوش اومدی 🌟")

bot.infinity_polling()
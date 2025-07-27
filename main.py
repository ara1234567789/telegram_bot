import telebot
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "سلام! به ربات من خوش اومدی 😊")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, f"شما گفتید: {message.text}")

bot.polling()

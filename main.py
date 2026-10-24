import telebot
import db
from config import TOKEN


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(
        message,
        "Salom! ToDo botga xush kelibsiz.\n\n"
        "Buyruqlar:\n"
        "/add Vazifa — vazifa qo'shish\n"
        "/list — vazifalarni ko'rish\n"
        "/done 1 — vazifani bajarilgan deb belgilash\n"
        "/delete 1 — vazifani o'chirish"
    )


@bot.message_handler(commands=["add"])
def add(message):
    matn = message.text.replace("/add", " ", 1).strip()


    if not matn:
        bot.reply_to(message, "Masalan : /add Dars qilish ")
        return

    db.vazifa_qosh(message.chat.id , matn)

    bot.reply_to(message, "Vazifa qo'shildi ! ")


@bot.message_handler(commands=["list"])
def vazifalar_listi(message):
    royxat = db.vazifa_ol(message.chat.id )

    if not royxat:
        bot.reply_to(message, " Hozircha vazifalar yoq .")
        return

    matn = ""

    for raq , vaz in enumerate(royxat, start=1):
        matn += f"{raq}. {vaz}\n"

    bot.reply_to(message, matn)


@bot.message_handler(commands=["done"])
def done(message):
    qismlar = message.text.split(maxsplit=1)

    if len(qismlar) != 2 or not qismlar[1].isdigit():
        bot.reply_to(message, "Masalan: /done 1")
        return

    raqam = int(qismlar[1])

    if db.vazifa_bajar(message.chat.id, raqam):
        bot.reply_to(message, "✅ Vazifa bajarildi!")
    else:
        bot.reply_to(message, "❌ Bunday vazifa yo'q.")


@bot.message_handler(commands=["delete"])
def delete(message):
    qismlar = message.text.split(maxsplit=1)

    if len(qismlar) != 2 or not qismlar[1].isdigit():
        bot.reply_to(message, "Masalan: /cancel 1")
        return

    raqam = int(qismlar[1])

    if db.vazifa_ochir(message.chat.id, raqam):
        bot.reply_to(message, "✅ Vazifa ochirildi !")
    else:
        bot.reply_to(message, "❌ Bunday vazifa yo'q.")


print("Bot ishga tushdi ")
bot.infinity_polling()





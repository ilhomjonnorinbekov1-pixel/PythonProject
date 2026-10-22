
import telebot
import json
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

royxatlar = {}


def yuklash():
    global royxatlar

    try:
        with open("todo.json", "r") as fayl:
            royxatlar = json.load(fayl)
    except (FileNotFoundError, json.JSONDecodeError):
        royxatlar = {}


def saqlash():
    with open("todo.json", "w") as fayl:
        json.dump(royxatlar, fayl, indent=4)


@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(
        message,
        "Salom! ToDo botga xush kelibsiz!\n\n"
        "/add - vazifa qo'shish\n"
        "/list - vazifalarni ko'rish\n"
        "/done 1 - vazifani bajarish\n"
        "/del 1 - vazifani o'chirish"
    )


@bot.message_handler(commands=["add"])
def add(message):
    bot.reply_to(message, "Vazifani yozing:")
    bot.register_next_step_handler(message, vazifa_qoshish)


def vazifa_qoshish(message):
    chat_id = str(message.chat.id)
    matn = message.text

    if chat_id not in royxatlar:
        royxatlar[chat_id] = []

    vazifa = {
        "matn": matn,
        "bajarildi": False
    }

    royxatlar[chat_id].append(vazifa)
    saqlash()

    bot.reply_to(message, "Vazifa qo'shildi!")


@bot.message_handler(commands=["list"])
def list_vazifalar(message):
    chat_id = str(message.chat.id)

    if chat_id not in royxatlar or len(royxatlar[chat_id]) == 0:
        bot.reply_to(message, "Vazifalar yo'q.")
        return

    javob = "Vazifalar:\n\n"

    for raqam, vazifa in enumerate(royxatlar[chat_id], start=1):
        if vazifa["bajarildi"]:
            belgi = "✅"
        else:
            belgi = "⬜"

        javob += str(raqam) + ". " + belgi + " " + vazifa["matn"] + "\n"

    bot.reply_to(message, javob)


@bot.message_handler(commands=["done"])
def done(message):
    chat_id = str(message.chat.id)
    qismlar = message.text.split()

    if len(qismlar) < 2 or not qismlar[1].isdigit():
        bot.reply_to(message, "Masalan: /done 1")
        return

    raqam = int(qismlar[1])

    if chat_id not in royxatlar:
        bot.reply_to(message, "Vazifalar yo'q.")
        return

    if raqam < 1 or raqam > len(royxatlar[chat_id]):
        bot.reply_to(message, "Bunday vazifa yo'q.")
        return

    royxatlar[chat_id][raqam - 1]["bajarildi"] = True
    saqlash()

    bot.reply_to(message, "Vazifa bajarildi!")


@bot.message_handler(commands=["del"])
def delete(message):
    chat_id = str(message.chat.id)
    qismlar = message.text.split()

    if len(qismlar) < 2 or not qismlar[1].isdigit():
        bot.reply_to(message, "Masalan: /del 1")
        return

    raqam = int(qismlar[1])

    if chat_id not in royxatlar:
        bot.reply_to(message, "Vazifalar yo'q.")
        return

    if raqam < 1 or raqam > len(royxatlar[chat_id]):
        bot.reply_to(message, "Bunday vazifa yo'q.")
        return

    royxatlar[chat_id].pop(raqam - 1)
    saqlash()

    bot.reply_to(message, "Vazifa o'chirildi!")


yuklash()

print("Bot ishga tushdi!")
bot.infinity_polling()

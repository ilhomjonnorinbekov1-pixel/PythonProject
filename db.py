import json

fayl = "todo.json"

vazifalar = {}


def yukla():
    global vazifalar

    try:
        with open(fayl, "r") as file:
            vazifalar = json.load(file)

    except FileNotFoundError:
        vazifalar = {}


def saqla():
    with open(fayl, "w") as file:
        json.dump(vazifalar, file, ensure_ascii=False, indent=2)


def vazifa_qosh(chat_id , matn):
    chat_id = str(chat_id)

    if chat_id not in vazifalar:
        vazifalar[chat_id] = []

    vazifalar[chat_id].append("[ ] " + matn)
    saqla()


def vazifa_ol(chat_id):
    chat_id = str(chat_id)
    return vazifalar.get(chat_id, [])


def vazifa_bajar(chat_id, raqam):
    chat_id = str(chat_id)
    royxat = vazifa_ol(chat_id)

    if raqam < 1 or raqam > len(royxat):
        return False

    idx = raqam - 1

    if royxat[idx].startswith("[x]"):
        return False

    royxat[idx] = "[x] " + royxat[idx][4:]
    saqla()
    return True


def vazifa_ochir(chat_id, raqam ):
    chat_id = str(chat_id)
    royxat = vazifa_ol(chat_id)

    if raqam < 1 or raqam > len(royxat):
        return  False

    royxat.pop(raqam - 1 )
    saqla()
    return True


yukla()



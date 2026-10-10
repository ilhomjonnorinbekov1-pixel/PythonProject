import constant
from Bankomat.son_sora import son_sora
import math
import random

def pul_qoyish():
    try:
        summa = son_sora("Summa kiriting : ")
        constant.balance += summa
        constant.tarix.append(f"+{summa}")
        print(f"Hisobingizga {summa} sum pul qoshildi")
        print(f"Sizning yangilangan balansingiz : {constant.balance}")

    except Exception as e:
        print("Pul qo'yishda xatolik : ", e)


def pul_olish():
    try:
        summa = son_sora("Qancha summa olmoqchisiz : ")

        if summa % 1000 != 0:
            raise ValueError("Summa 1000 ga karrali bo'lishi kerak")

        if summa > constant.balance:
            raise ValueError("Hisobingizda mablag' yetarli emas!")

        if summa > 10000000:
            raise ValueError("Bir urinishda 10 milliondan ko'p summa yecha olmaysiz!")

        komissiya = math.ceil(summa * 0.01)
        jami = summa + komissiya

        if jami > constant.balance:
            raise ValueError("Komissiya bilan summa balansingizdan oshib ketdi")

        constant.balance -= jami

        chek = random.randint(100000, 999999)

        constant.tarix.append(f"-{summa}")

        print(f"Chek raqami: {chek}")
        print(f"Olingan summa: {summa}")
        print(f"Komissiya: {komissiya}")
        print(f"Jami yechilgan summa: {jami}")
        print(f"Balance holati: {constant.balance}")

    except ValueError as e:
        print("Xato:", e)
    except Exception as e:
        print("Kutilmagan xato:", e)







import math
import random

balance = 250000
pin = "1234"
tarix = []
bloklangan = False

def pin_tekshirish():
    global bloklangan

    for urinish in range(1,4):
        try:
            kiritilgan_pin = input("pin kodni kiriting : ").strip()
            if not kiritilgan_pin:
                raise ValueError("Pin kod bo'sh qolmasligi kerak !")
            if not kiritilgan_pin.isdigit():
                raise ValueError("Pin kodga faqat son kiritishingiz kerak ! ")
            if kiritilgan_pin != pin:
                raise ValueError("Kiritilgan pin kod Xato ! ")
            print("Pin-Kod to'gri . Xush kelibsiz ! ")
            return True
        except ValueError as e:
            print(f"Xato: {e}")
            print(f"Qolgan urinish: {3 - urinish}")

    bloklangan = True
    print("3 marta xato kiritdingiz . Karta bloklandi ! ")
    return False

def son_sora(number ):
    while True:
        try:
            son = input(number).strip()
            if not son:
                raise ValueError("Bo'sh bolmasligi kerak ")
            if not son.isdigit():
                raise ValueError("Faqat son kiritishingiz kerak ")
            son = int(son)
            if son <= 0 :
                raise ValueError("Musbat son bo'lishi kerak! ")
            return son
        except ValueError as e:
            print("Xato", e)


def pul_qoyish():
    global balance
    try:
        summa = son_sora("Summa kiriting : ")
        balance += summa
        tarix.append(f"+{summa}")
        print(f"Hisobingizga {summa} sum pul qoshildi ")
        print(f"Sizning yangilangan balansingiz : {balance}")

    except Exception as e :
        print("Pul qo'yishda xatolik : ", e)

def pul_olish():
    global balance
    try:
        summa = son_sora("Qancha summa olmoqchisiz :")
        if summa % 1000 != 0:
            raise ValueError("Summa 1000 ga karrali bolishi kerak ")
        if summa > balance:
            raise ValueError("Hisobingizda mablag' yetarli emas ! ")
        if summa > 10000000:
            raise ValueError("Bir urunishda 10 milliondan ko'p summa yecha olmaysiz  ! ")

        kamissiya = math.ceil(summa* 0.01)
        jami = summa + kamissiya

        if jami > balance:
            raise ValueError("kamissiya bilan summa oshib ketti balansda pul yetarli emas  ")

        balance -= jami

        chek = random.randint(100000, 999999)

        tarix.append(f"-{summa}")

        print(f"Chek raqami {chek}")
        print(f"Olingan summa : {summa}")
        print(f"komissiya : {kamissiya}")
        print(f"Jami yechilgan summa : {jami}")
        print(f"Balance holati : {balance}")

    except ValueError as e :
        print("Xato :", e)
    except Exception as e :
        print("Kutilmagan xato :", e)

def balans_korsatish():
    print(f"\n Balansingiz : {balance} so'm ")

def tarix_korsatish():
    print("\n --- Operatsiyalar tarixi ---")

    if not tarix:
        print("Tarix bo'sh ")
        return
    for i , money in enumerate(tarix, 1):
        print(f"{i}. {money} so'm")

    tushum = list(filter(lambda x : x.startswith("+") , tarix))

    jami_tushum = sum(map(lambda x: int(x) , tushum))

    print(f"\nJami qoyilgan summa {jami_tushum} so'm ! ")



def menu():
    while True:
        print("\n" + "=" * 35)
        print("          BANKOMAT")
        print("=" * 35)
        print("1. Balansni ko'rish")
        print("2. Pul qo'yish")
        print("3. Pul olish")
        print("4. Operatsiyalar tarixi")
        print("0. Chiqish")
        print("=" * 35)

        tanlov = input("Bo'limni tanlang :").strip()
        if tanlov == "1":
            balans_korsatish()
        elif tanlov == "2":
            pul_qoyish()
        elif tanlov == "3":
            pul_olish()
        elif tanlov == "4":
            tarix_korsatish()
        elif tanlov == "0":
            print("Dastur tugadi . Salomad bo'ling  ! ")
            break
        else:
            print("Noto'g'ri bo'lim tanlandi ! ")


def main():
    if pin_tekshirish():
        menu()
main()












from constant import pin


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






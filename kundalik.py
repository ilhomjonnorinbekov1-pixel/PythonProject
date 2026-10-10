from datetime import datetime
def yozuv_qoshish():

    matn = input("Kundalik rejalaringiz : ")

    sana = datetime.now()

    with open("kundalik.txt" , "a") as file:
        file.write(f"{sana}  |  {matn}\n")\

    print("Yozuv  qo'shildi ! ")

def hammasini_oqish():
    try:
        with open("kundalik.txt", "r") as file:
            for i in file:
                print(i.strip())

    except FileNotFoundError:
        print("Hali kundalik rejalar yozilmadi !  ")


def qidirish():
    search = input("Qidirmoqchi bo'lgan gapni kiriting : ").lower()
    try:
        with open("kundalik.txt", "r") as file:
            topildi = False

            for i in file:
                if search in i.lower():
                    print(i.strip())
                    topildi = True

            if not topildi:
                print("Bunday yozuv topilmadi ! ")

    except FileNotFoundError:
        print("Hali kundalikga rejalar yozilmagan ")


while True:
    print("""
===== KUNDALIK =====
1. Yozuv qo'shish
2. Hammasini o'qish
3. Qidirish
0. Chiqish
""")

    tanlov = input("Bo'lim tanlang : ")

    if tanlov == "1":
        yozuv_qoshish()
    elif tanlov == "2":
        hammasini_oqish()
    elif tanlov == "3":
        qidirish()
    elif tanlov == "0":
        print("Dastur tugadi ")
        break
    else:
        print("Mavjud bo'lmagan bo'lim ! ")




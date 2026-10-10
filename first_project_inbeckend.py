ombor = {}


def add_product():
    name = input("Mahsulot nomi: ").strip().lower()

    if name in ombor:
        print("Bu mahsulot omborda bor!")
        return

    try:
        price = int(input("Mahsulot narxi: "))
        number = int(input("Mahsulot soni: "))

        if price <= 0 or number <= 0:
            print("Narx va son 0 dan katta bo'lishi kerak!")
            return

        ombor[name] = {
            "narxi": price,
            "soni": number
        }

        print("Mahsulot muvaffaqiyatli omborga saqlandi!")
        print(ombor)

    except ValueError:
        print("Narx va sonni faqat raqam bilan kiriting!")


def all_product():
    if not ombor:
        print("Ombor bo'sh!")
        return

    print("Sizning ombordagi mahsulotlaringiz:")

    for name, info in ombor.items():
        print(
            f"{name} | "
            f"Narxi: {info['narxi']} so'm | "
            f"Soni: {info['soni']} dona"
        )


def search_product():
    name = input("Qaysi mahsulotni qidiramiz: ").strip().lower()

    if name in ombor:
        print(
            f"Mahsulot: {name}\n"
            f"Narxi: {ombor[name]['narxi']} so'm\n"
            f"Soni: {ombor[name]['soni']} dona"
        )
    else:
        print("Omborda bu mahsulot yo'q!")


def update():
    yangi = input("Qaysi mahsulotni yangilaymiz: ").strip().lower()

    if yangi not in ombor:
        print("Bunday mahsulot omborda yo'q!")
        return

    tanlov2 = input("""
1 — Kirim (soni oshadi)
2 — Chiqim (soni kamayadi)
3 — Yangi narx
>>> Tanlang: """)

    try:
        if tanlov2 == "1":
            a = int(input("Nechta keldi: "))

            if a <= 0:
                print("Son 0 dan katta bo'lishi kerak!")
                return

            ombor[yangi]["soni"] += a
            print("Kirim muvaffaqiyatli amalga oshirildi!")

        elif tanlov2 == "2":
            b = int(input("Nechta chiqdi: "))

            if b <= 0:
                print("Son 0 dan katta bo'lishi kerak!")
                return

            if b <= ombor[yangi]["soni"]:
                ombor[yangi]["soni"] -= b
                print("Chiqim muvaffaqiyatli amalga oshirildi!")
            else:
                print("Omborda buncha mahsulot yo'q!")

        elif tanlov2 == "3":
            c = int(input("Yangi narx: "))

            if c <= 0:
                print("Narx 0 dan katta bo'lishi kerak!")
                return

            ombor[yangi]["narxi"] = c
            print("Narx muvaffaqiyatli yangilandi!")

        else:
            print("Noto'g'ri tanlov!")

    except ValueError:
        print("Faqat raqam kiriting!")


def delete_product():
    tozalash = input(
        "Qaysi mahsulotni o'chiramiz: "
    ).strip().lower()

    if tozalash not in ombor:
        print("Bunday mahsulot omborda yo'q!")
        return

    sorov = input(
        f"{tozalash} rostan ham o'chirilsinmi (ha/yo'q): "
    ).strip().lower()

    if sorov == "ha":
        ombor.pop(tozalash)
        print("Mahsulot o'chirildi!")
    else:
        print("Amaliyot bekor qilindi!")


def total_product():
    umumiy = 0

    for info in ombor.values():
        umumiy += info["soni"] * info["narxi"]

    print(f"Ombordagi umumiy boylik: {umumiy} so'm")


def main():
    print("""
========================================
       📦 OMBORXONA TIZIMI v1.0
========================================
""")

    while True:
        try:
            tanlov = int(input("""
1 — Mahsulot qo'shish
2 — Barcha mahsulotlar
3 — Qidirish
4 — Yangilash (kirim/chiqim/narx)
5 — O'chirish
6 — Umumiy qiymat
0 — Chiqish
>>> Bo'limni tanlang: """))

        except ValueError:
            print("Iltimos, faqat raqam kiriting!")
            continue

        if tanlov == 1:
            add_product()

        elif tanlov == 2:
            all_product()

        elif tanlov == 3:
            search_product()

        elif tanlov == 4:
            update()

        elif tanlov == 5:
            delete_product()

        elif tanlov == 6:
            total_product()

        elif tanlov == 0:
            print("Dastur to'xtadi!")
            break

        else:
            print("Noto'g'ri bo'lim tanlandi!")


main()





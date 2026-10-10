kutubxona = {}
qarzdorlar = {}


def add_book():
    name = input("Kitob nomi: ").strip().lower()

    if not name:
        print("Kitob nomini bo'sh qoldirmang!")
        return

    if name in kutubxona:
        print("Bu kitob kutubxonada bor!")
        return

    try:
        author = input("Kitob muallifi: ").strip()
        number_book = int(input("Nechta nusxa: "))

        if not author:
            print("Muallif nomini bo'sh qoldirmang!")
            return

        if number_book <= 0:
            print("Nusxa soni 0 dan katta bo'lishi kerak!")
            return

        kutubxona[name] = {
            "Muallif": author,
            "Mavjud": number_book,
            "Jami": number_book
        }

        print("Kitob muvaffaqiyatli saqlandi!")

    except ValueError:
        print("Nusxa sonini faqat raqam bilan yozing!")


def all_books():
    if not kutubxona:
        print("Kutubxona bo'sh!")
        return

    print("\n===== BARCHA KITOBLAR =====")

    for name, book in kutubxona.items():
        print(
            f"Kitob: {name} | "
            f"Muallif: {book['Muallif']} | "
            f"Mavjud: {book['Mavjud']} dona | "
            f"Jami: {book['Jami']} dona"
        )


def search_book():
    name = input("Qaysi kitobni qidirmoqchisiz: ").strip().lower()

    if name in kutubxona:
        book = kutubxona[name]
        print("\n===== KITOB MA'LUMOTI =====")
        print(f"Kitob: {name}")
        print(f"Muallif: {book['Muallif']}")
        print(f"Mavjud: {book['Mavjud']} dona")
        print(f"Jami: {book['Jami']} dona")
    else:
        print("Kutubxonada bu kitob yo'q!")


def rent_book():
    name = input("Qaysi kitob beriladi: ").strip().lower()

    if name not in kutubxona:
        print("Bunday kitob kutubxonada yo'q!")
        return

    if kutubxona[name]["Mavjud"] <= 0:
        print("Bu kitobning hozircha nusxasi qolmagan!")
        return

    ism = input("Kimga beriladi: ").strip()

    if not ism:
        print("Ismni bo'sh qoldirmang!")
        return

    kutubxona[name]["Mavjud"] -= 1

    if ism not in qarzdorlar:
        qarzdorlar[ism] = {}

    qarzdorlar[ism][name] = qarzdorlar[ism].get(name, 0) + 1

    print(
        f'"{name}" kitobi {ism}ga berildi. '
        f"Qoldi: {kutubxona[name]['Mavjud']} dona."
    )


def comeback_book():
    if not qarzdorlar:
        print("Hozircha hech kimda kitob yo'q!")
        return

    ism = input("Kim qaytaryapti: ").strip()

    if ism not in qarzdorlar:
        print("Bu odamning qarzdor kitobi yo'q!")
        return

    print("\n===== QARZDOR KITOBLAR =====")
    for name, soni in qarzdorlar[ism].items():
        print(f"{name} — {soni} dona")

    kitob = input("Qaysi kitob qaytariladi: ").strip().lower()

    if kitob not in qarzdorlar[ism]:
        print("Bu odamda bunday kitob yo'q!")
        return

    kutubxona[kitob]["Mavjud"] += 1
    qarzdorlar[ism][kitob] -= 1

    if qarzdorlar[ism][kitob] == 0:
        del qarzdorlar[ism][kitob]

    if not qarzdorlar[ism]:
        del qarzdorlar[ism]

    print(f'"{kitob}" kitobi qaytarib olindi. Rahmat!')


def show_debtors():
    if not qarzdorlar:
        print("Hozircha qarzdorlar yo'q!")
        return

    print("\n===== QARZDORLAR RO'YXATI =====")

    for ism, books in qarzdorlar.items():
        print(f"\n{ism}:")
        for name, soni in books.items():
            print(f"  - {name} x{soni}")


def delete_book():
    name = input("Qaysi kitobni o'chirmoqchisiz: ").strip().lower()

    if name not in kutubxona:
        print("Bunday kitob topilmadi!")
        return

    for ism, books in qarzdorlar.items():
        if name in books:
            print("Bu kitob hozir qarzga berilgan!")
            print("Avval kitob qaytarib olinishi kerak.")
            return

    del kutubxona[name]
    print(f'"{name}" kitobi kutubxonadan ochirildi!')


def main():
    print("""
============================================
        📚 KUTUBXONA TIZIMI v1.0
============================================
""")

    while True:
        print("""
1 — Kitob qo'shish
2 — Barcha kitoblar
3 — Kitob qidirish
4 — Kitobni ijaraga berish
5 — Kitobni qaytarib olish
6 — Qarzdorlar ro'yxati
7 — Kitobni o'chirish
0 — Chiqish
""")

        try:
            tanlov = int(input(">>> Bo'limni tanlang: "))
        except ValueError:
            print("Iltimos, faqat raqam kiriting!")
            continue

        if tanlov == 1:
            add_book()

        elif tanlov == 2:
            all_books()

        elif tanlov == 3:
            search_book()

        elif tanlov == 4:
            rent_book()

        elif tanlov == 5:
            comeback_book()

        elif tanlov == 6:
            show_debtors()

        elif tanlov == 7:
            delete_book()

        elif tanlov == 0:
            print("Dastur to'xtadi. Xayr!")
            break

        else:
            print("Noto'g'ri bo'lim tanlandi!")



main()





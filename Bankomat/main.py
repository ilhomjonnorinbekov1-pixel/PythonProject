

from Bankomat.show_money import balans_korsatish
from Bankomat.add_money import pul_qoyish
from Bankomat.add_money import pul_olish
from Bankomat.show_money import tarix_korsatish
from Bankomat.pin_tekshiruv import pin_tekshirish


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
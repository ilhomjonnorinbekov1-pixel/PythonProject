#
# import math
#
# r = float(input("Radiusni kiriting: "))
#
# yuza = math.pi * r ** 2
# uzunlik = 2 * math.pi * r
#
# print(f"Doira yuzi: {yuza:.2f}")
# print(f"Aylana uzunligi: {uzunlik:.2f}")
#
#
# import math
#
# N = int(input("O'quvchilar soni: "))
# K = int(input("Avtobus sig'imi: "))
#
# avtobus = math.ceil(N / K)
#
# print(f"Kerakli avtobuslar soni: {avtobus}")
import datetime
import random

from def_mavzusi import chegirma

for i in range(10):
    zar1 = random.randint(1, 6)
    zar2 = random.randint(1, 6)

    yigindi = zar1 + zar2

    print(f"{i + 1}-tashlash:")

    if yigindi == 7:
        print("OMAD!")
    else:
        print(f"Yig'indi: {yigindi}")



import random
harflar = "abcdefgh123456789"

parol = ""
for i in range(8):
    parol += random.choice(harflar)

print(parol)


# from datetime import datetime
# yil = int(input("Tug'ilgan yilingizni kiriting : "))
# now = datetime.now()
# age = now.year - yil
# print(f"Sizning yoahingiz {age} da ")


kub = lambda x: x ** 3
juftmi = lambda x: x % 2 == 0
kattami = lambda x,y : max(x,y)
print(kub(5))
print(juftmi(4))
print(kattami(78,45))


narxlar = [10000, 25000, 40000, 8000]
chegirma = list(map(lambda x: int(x * 0.85), narxlar))

print(chegirma)


ballar = [45, 78, 90, 32, 65, 88, 51]
oltmish_plus = list(filter(lambda x: x > 60, ballar))
juft = list(filter(lambda x: x % 2 == 0,ballar))
print(ballar)
print("60 + ballar  >>>" , oltmish_plus)
print("Juft ballar  >>>", juft)


def yigindi(n):

    if n == 1:
        return 1
    return n + (yigindi(n - 1))



print(yigindi(100))




import random

lotereya = set(random.sample(range(1, 37), 6))

foydalanuvchi = set()

for i in range(6):
    son = int(input(f"{i + 1}-sonni kiriting: "))
    foydalanuvchi.add(son)

togri = lotereya.intersection(foydalanuvchi)

print("Lotereya sonlari:", lotereya)
print("Sizning sonlaringiz:", foydalanuvchi)
print("To'g'ri kelgan sonlar:", togri)
print("Jami:", len(togri))


def ochil(n):
    print(f"{n}-quti ochildi...")

    if n == 1:
        print("Eng kichigi!")
        return

    ochil(n - 1)

    print(f"{n}-quti yopildi...")


ochil(4)











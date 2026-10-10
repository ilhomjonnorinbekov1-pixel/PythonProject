from constant import tarix, balance



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







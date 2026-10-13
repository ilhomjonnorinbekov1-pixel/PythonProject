class Book:
    def __init__(self, kitob):
        self.kitob = kitob

    def __str__(self):
        return f"Bizning kitobimizning nomi {self.kitob}"


    def __eq__(self, other):
       return self.kitob == other.kitob

a = Book("Psixalagik urush ! ")
b = Book("Mexrobdan chayon")
print(a)
print(a == b)


class Catalog:
    def __init__(self):
        self.__items = []

    def add(self,item):
        self.__items.append(item)

    def __len__(self):
        return len(self.__items)

    def __getitem__(self, index ):
        return self.__items[index]


catalog = Catalog()

catalog.add(a)
catalog.add(b)
print(len(catalog))
print(catalog[0])
print(catalog[1])

# Uy ishi
class BankAccount:
    bank_shoti = 0
    def __init__(self,hisob, balance ):
        self.hisob = hisob
        self.__balance = balance
        BankAccount.bank_shoti += 1

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, son):
        if son < 0 :
            raise ValueError("Manfiy son mumkin emas ")

        self.__balance = son

    @classmethod
    def hisob_soni(cls):
        return cls.bank_shoti

    @staticmethod
    def valyuta_kursi(usd):
        kurs = 12000
        return usd * kurs

    def __str__(self):
        return f"Egasi : {self.hisob} | Balance : {self.balance}"

    def __eq__(self, other):
        return self.balance == other.balance

    def __gt__(self, other):
        return self.balance > other.balance

    def __add__(self, other):
        return BankAccount(self.hisob + "va" + other.hisob,
        self.balance + other.balance)

acc1 = BankAccount("Ibrohim ", 5000000)
acc2 = BankAccount("Samandar", 14000000)
acc3 = BankAccount("Abu", 45000000)

print(acc1)
print(acc2 == acc3)
print(acc1 > acc2)
bank_shoti = [acc1,acc2,acc3]
a = sorted(bank_shoti)

for i in a:
    print(i)

print(BankAccount.hisob_soni())
print(BankAccount.valyuta_kursi(100))













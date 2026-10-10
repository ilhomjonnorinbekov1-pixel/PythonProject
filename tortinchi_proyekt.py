import logging

#

logging.basicConfig(level=logging.DEBUG,
                    filename='avtosalon.log',
                    filemode='a',
                    format='%(asctime)s - %(levelname)s - %(message)s')


# darajalar
# logging.debug("tafsilot")       # 10 < 30 → ko'rinmaydi
# logging.info("axborot")         # 20 < 30 → ko'rinmaydi
# logging.warning("diqqat!")      # 30 ≥ 30 → ✅ chiqadi
# logging.error("xato!")         # 40 ≥ 30 → ✅ chiqadi





class Avto:
    __jami = 0

    def __init__(self, model, narx, egasi=None, rang="oq"):
        self.model = model
        self.narx = narx
        self.rang = rang
        self.egasi = egasi

        Avto.__jami += 1

    def get_info(self):
        if self.egasi is None:
            return f"{self.rang} {self.model} - {self.narx}$ (Sotuvda)"
        else:
            holat = f"egasi: {self.egasi.ism}"
            return f"{self.rang} {self.model} - {self.narx}$ ({holat})"

    def __str__(self):
        return self.get_info()

    def __gt__(self, other):
        return self.narx > other.narx

    @classmethod
    def jami_yaratilgan(cls):
        return cls.__jami


class ElektroAvto(Avto):
    def __init__(self, model, narx, zaryad_km, egasi=None, rang="oq"):
        super().__init__(model, narx, egasi, rang)
        self.zaryad_km = zaryad_km

    def get_info(self):
        if self.egasi is None:
            return f" {self.rang} {self.model} - {self.narx}$ | zaryad: {self.zaryad_km} km (Sotuvda)"
        else:
            holat = f"egasi: {self.egasi.ism}"
            return f" {self.rang} {self.model} - {self.narx}$ | zaryad: {self.zaryad_km} km ({holat})"


class Mijoz:
    def __init__(self, ism, tel):
        self.ism = ism
        self.tel = tel

    def get_info(self):
        pass


avto = ElektroAvto("Tesla", 40000, 500, None, "Qora")

avto1 = Avto("Malibu", 40000)

avto2 = Avto("Damas", 5000)

avtolar = [avto1, avto2]
print(f" Narxi qimmati : {max(avtolar)}")

print(avto1 > avto2)

avto.egasi = Mijoz("Alijon", "+9984530805")
print(avto.get_info())


class Salon:
    def __init__(self, nom):
        self.nom = nom
        self.__avtolar = []

    def add(self, avto):
        self.__avtolar.append(avto)
        print("Avto qo'shildi!", avto.get_info())
        logging.info(f" {avto }Avtosalonga mashina qo'shildi ")


    def hammasi(self):

        for i in self.__avtolar:
            print(i)

    def sotuvda(self):
        sotilyapti = []

        for i in self.__avtolar:
            if i.egasi is None:
                sotilyapti.append(i)

        return sotilyapti

    def eng_qimmat(self):
        avtolar1 = self.sotuvda()

        if not avtolar1:
            return None

        return max(avtolar1)

    def sot(self, raqam, mijoz):

        if raqam < 0 or raqam >= len(self.__avtolar):
            print( "Noto'gri raqam kiritdingiz ! ")
            logging.warning("Notogri son kiritildi ! ")


        mashina = self.__avtolar[raqam]

        if mashina.egasi is not None:
            return "Afsuski allaqachon sotilgan ! "

        mashina.egasi = mijoz
        print(f"SOTILDI ! {mashina}")

    def __len__(self):
        return len(self.__avtolar)

    def __getitem__(self, item):
        return self.__avtolar[item]


salon = Salon("Ustudy motors")

avto1 = Avto("Malibu", 40000, rang="qora")
avto2 = ElektroAvto("Tesla Model 3", 90000, 500)
avto3 = Avto("Damas", 5000)

salon.add(avto1)
salon.add(avto2)
salon.add(avto3)

while True:
    print(f"""
    ===== {salon.nom} | avtolar: {len(salon)} =====
    1. Avto qo'shish
    2. Elektromobil qo'shish
    3. Hammasini ko'rish
    4. Sotish
    5. Eng qimmat avto
    0. Chiqish
    """)

    tanlov = input("Tanlang : ")

    if tanlov == "1":
        model = input("Model : ")

        try:
            narx = int(input("Narx : "))

        except ValueError("Narx son bo'lishi kerak ! "):
            continue

        rang = input("Rang : ").strip()
        if not rang:
            rang = "oq"

        salon.add(Avto(model, narx, rang=rang))

    elif tanlov == '2':
        model = input("Model : ")

        try:
            narx = int(input("Narx: "))
            zaryad = int(input("Zaryad km: "))

        except ValueError("Narx va Zaryad son bo'lishi kerak ! "):
            continue

        rang = input("Rang : ").strip()

        if not rang:
            rang = "oq"

        salon.add(ElektroAvto(model, narx, zaryad, rang=rang))

    elif tanlov == "3":
        print("======= Barcha avtolar =======")
        salon.hammasi()

    elif tanlov == "4":

        try:
            raqam = int(input("Avto raqamni kiriting ; "))

        except ValueError("Faqat son kiriting : "):
            continue

        ism = input("Ismingiz : ")
        tel = input("Telefon raqamingiz : ")

        mijoz = Mijoz(ism, tel)

        salon.sot(raqam, mijoz)

    elif tanlov == "5":
        avto = salon.eng_qimmat()

        if avto:
            print(f"Eng qimmat avto : {avto}")

        else:
            print("Sotuvda mashina yoq ")

    elif tanlov == "0":
        print("Dastur tugadi ")
        break
    else:
        print("Notog'ri tanlov !!! ")

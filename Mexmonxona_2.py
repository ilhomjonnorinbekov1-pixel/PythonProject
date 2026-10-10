
import json
import logging


logging.basicConfig(
    filename="jurnal.log",
    filemode="a",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(funcName)s - %(message)s",

)


class Mehmon:
    def __init__(self, ism, tel):
        self.ism = ism
        self.tel = tel

    def __str__(self):
        return f"Mehmon: {self.ism} | Telefon: {self.tel}"


class Xona:
    jami = 0

    def __init__(self, raqam, narx, sigim=2):
        self.raqam = raqam
        self.narx = narx
        self.sigim = sigim
        self.mehmon = None
        self.__band = False

        Xona.jami += 1

    def band_mi(self):
        return self.__band

    def band_qil(self, mehmon):
        if self.__band:
            return False

        self.__band = True
        self.mehmon = mehmon
        return True

    def boshat(self):
        if not self.__band:
            return None

        eski = self.mehmon
        self.__band = False
        self.mehmon = None

        return eski

    def turi(self):
        return "Oddiy"

    def __str__(self):
        if self.__band:
            holat = f"Band ({self.mehmon.ism})"
        else:
            holat = "Bo'sh"

        return (
            f"{self.raqam}-xona | {self.turi()} | "
            f"{self.narx} so'm | {self.sigim} kishi | {holat}"
        )

    def __gt__(self, other):
        return self.narx > other.narx


class Lyuks(Xona):
    def __init__(self, raqam, narx):
        super().__init__(raqam, narx, sigim=4)
        self.nonushta = True

    def turi(self):
        return "Lyuks"

    def __str__(self):
        return super().__str__() + " + nonushta"


class Mehmonxona:
    def __init__(self, nom="Ustudy Hotel"):
        self.nom = nom
        self.__xonalar = []

    def top(self, raqam):
        for xona in self.__xonalar:
            if xona.raqam == raqam:
                return xona

        return None

    def xona_qosh(self, xona):
        if self.top(xona.raqam):
            print("Bu raqamli xona mavjud!")
            logging.warning(f"{xona.raqam}-xona avvaldan mavjud")
            return

        self.__xonalar.append(xona)

        print(f"{xona.raqam}-xona qo'shildi ({xona.turi()})")
        logging.info(f"{xona.raqam}-xona qo'shildi ({xona.turi()})")

    def joylash(self, raqam, mehmon):
        xona = self.top(raqam)

        if xona is None:
            print("Bunday xona yo'q!")
            logging.warning(f"{raqam}-xona topilmadi")
            return

        if xona.band_mi():
            print(f"{raqam}-xona allaqachon band!")
            logging.warning(f"{raqam}-xona allaqachon band")
            return

        xona.band_qil(mehmon)

        print(f"{mehmon.ism} {raqam}-xonaga joylashdi")
        logging.info(f"{mehmon.ism} {raqam}-xonaga joylashdi")

    def boshat(self, raqam):
        xona = self.top(raqam)

        if xona is None:
            print("Bunday xona yo'q!")
            logging.warning(f"{raqam}-xona topilmadi")
            return

        if not xona.band_mi():
            print("Xona shundoq ham bo'sh!")
            logging.warning(f"{raqam}-xona allaqachon bo'sh")
            return

        mehmon = xona.boshat()

        print(f"{mehmon.ism} {raqam}-xonadan chiqdi!")
        logging.info(f"{mehmon.ism} {raqam}-xonadan chiqdi")

    def hammasi(self):
        if len(self.__xonalar) == 0:
            print("Xonalar mavjud emas!")
            return

        for xona in self.__xonalar:
            print(xona)

    def boshlar(self):
        bosh_xonalar = []

        for xona in self.__xonalar:
            if not xona.band_mi():
                bosh_xonalar.append(xona)

        return bosh_xonalar

    def eng_qimmat(self):
        if not self.__xonalar:
            return None

        return max(self.__xonalar)

    def daromad(self):
        jami = 0

        for xona in self.__xonalar:
            if xona.band_mi():
                jami += xona.narx

        return jami

    def saqla(self):
        malumot = []

        for xona in self.__xonalar:
            xona_info = {
                "raqam": xona.raqam,
                "narx": xona.narx,
                "sigim": xona.sigim,
                "lyuks": isinstance(xona, Lyuks),
                "mehmon": None
            }

            if xona.mehmon:
                xona_info["mehmon"] = {
                    "ism": xona.mehmon.ism,
                    "tel": xona.mehmon.tel
                }

            malumot.append(xona_info)

        with open("mehmonxona.json", "w", encoding="utf-8") as file:
            json.dump(
                malumot,
                file,
                ensure_ascii=False,
                indent=4
            )

        print(f"{len(self)} ta xona saqlandi")
        logging.info(f"{len(self)} ta xona JSON fayliga saqlandi")

    @classmethod
    def yukla(cls, nom="Ustudy Hotel"):
        mehmonxona = cls(nom)

        try:
            with open("mehmonxona.json", "r", encoding="utf-8") as file:
                malumot = json.load(file)

            for i in malumot:
                if i["lyuks"]:
                    xona = Lyuks(i["raqam"], i["narx"])
                else:
                    xona = Xona(
                        i["raqam"],
                        i["narx"],
                        i["sigim"]
                    )

                if i["mehmon"]:
                    mehmon = Mehmon(
                        i["mehmon"]["ism"],
                        i["mehmon"]["tel"]
                    )
                    xona.band_qil(mehmon)

                mehmonxona.__xonalar.append(xona)

            print(f"{len(mehmonxona)} ta xona yuklandi")
            logging.info(f"{len(mehmonxona)} ta xona JSON faylidan yuklandi")

        except FileNotFoundError:
            print("Saqlangan fayl topilmadi. Mehmonxona bo'sh.")
            logging.warning("JSON fayli topilmadi")

        except json.JSONDecodeError:
            print("JSON fayli noto'g'ri formatda!")
            logging.error("JSON faylini o'qishda xatolik")

        return mehmonxona

    def __len__(self):
        return len(self.__xonalar)

    def __getitem__(self, item):
        return self.__xonalar[item]

    def __str__(self):
        return f"{self.nom}: {len(self)} ta xona"


def main():
    m = Mehmonxona.yukla()

    while True:
        print("\n=== MEHMONXONA ===")
        print("1. Xona qo'shish")
        print("2. Barcha xonalar")
        print("3. Mehmon joylash")
        print("4. Xonani bo'shatish")
        print("5. Bo'sh xonalar")
        print("6. Eng qimmat xona")
        print("7. Daromadni ko'rish")
        print("8. Saqlash")
        print("0. Chiqish")

        try:
            tanlov = int(input("Tanlang: "))

            if tanlov == 1:
                raqam = int(input("Xona raqami: "))
                narx = int(input("Xona narxi: "))
                tur = input("Turi (oddiy/lyuks): ").lower()

                if tur == "oddiy":
                    xona = Xona(raqam, narx)
                elif tur == "lyuks":
                    xona = Lyuks(raqam, narx)
                else:
                    print("Noto'g'ri xona turi!")
                    logging.warning("Noto'g'ri xona turi kiritildi")
                    continue

                m.xona_qosh(xona)

            elif tanlov == 2:
                m.hammasi()

            elif tanlov == 3:
                raqam = int(input("Xona raqami: "))
                ism = input("Mehmon ismi: ")
                tel = input("Telefon: ")

                mehmon = Mehmon(ism, tel)
                m.joylash(raqam, mehmon)

            elif tanlov == 4:
                raqam = int(input("Xona raqami: "))
                m.boshat(raqam)

            elif tanlov == 5:
                bosh = m.boshlar()
                print(f"Bo'sh xonalar: {len(bosh)} ta")

                for xona in bosh:
                    print(xona)

            elif tanlov == 6:
                xona = m.eng_qimmat()

                if xona:
                    print(f"Eng qimmat xona: {xona}")
                else:
                    print("Xonalar mavjud emas.")

            elif tanlov == 7:
                print(f"Daromad: {m.daromad()} so'm")

            elif tanlov == 8:
                m.saqla()

            elif tanlov == 0:
                m.saqla()
                print("Xayr!")
                break

            else:
                print("Noto'g'ri tanlov!")
                logging.warning("Menyuda noto'g'ri tanlov kiritildi")

        except ValueError:
            print("Xato! Son kiritishingiz kerak.")
            logging.error("Son kiritilishi kerak bo'lgan joyga noto'g'ri qiymat kiritildi")

        finally:
            print(f"[Jami xonalar: {len(m)}]")



main()












































class Author:
    def __init__(self, name):
        self.name = name


class LibraryItem:
    def __init__(self, title, subject = "Umumiy"):
        self.title = title
        self.subject = subject


    def get_info(self):
        return f"{self.title}  | : {self.subject}"

class Book(LibraryItem):
    def __init__(self,title,author, subject = "Umumiy" ,  ):
        super().__init__(title,subject)
        self.author = author

    def get_info(self):
        return f" Kitob: {self.title} — {self.author.name} | mavzu: {self.subject}"


class Magazin(LibraryItem):
    def __init__(self,title, issue, subject = "Umumiy" ):
        super().__init__(title,subject)
        self.issue = issue

    def get_info(self):
        return f"Jurnal : {self.title}  | : {self.issue} - son"


class DVD(LibraryItem):
    def __init__(self,title, director,  subject = "Umumiy" ):
        super().__init__(title,subject)
        self.director = director

    def get_info(self):
        return f'DVD : "{self.title}" - rej : {self.director}  || janr: {self.subject}'


class Catalog:
    def __init__(self):
        self.__items = []

    def add(self,item):
        self.__items.append(item)
        print(f"Katalogga qo'shildi : {item.get_info()}")


    def search(self,soz):
        qidiruv_royxat = []

        for kitob in self.__items:
            if soz.lower() in kitob.title.lower():
                qidiruv_royxat.append(kitob)

        return qidiruv_royxat

    def hammasi(self):
        for kitob in self.__items:
            print(kitob.get_info())


    def jami(self):

        return len(self.__items)



    def saqla(self,fayl_nomi):
        with open(fayl_nomi, "w",) as fayl:
            for i in self.__items:
                fayl.write(i.get_info() + "\n")

        print("Catalogga saqlandi ! ")



    def yukla(self,fayl_nomi):
        try:
            with open(fayl_nomi,  "r", ) as fayl:
                self.__items.clear()
                for qator in fayl:
                    print(qator.strip())

        except FileNotFoundError:
            print("Hali saqlangan katalog topilmadi ! ")




def kitob_qoshish(catalog):
    title = input("Kitob nomi : ")
    author_name = input("Muallif kim : ")
    subject = input("Mavzu : ")


    author = Author(author_name)
    book = Book(title,author,subject)

    catalog.add(book)


def jurnal_qoshish(catalog):
    title = input("Jurnal nomi : ")
    try:
        issue = int(input("nechanchi son : "))
    except ValueError:
        print("Faqat son kiriting : ")

        return
    magazin = Magazin(title,issue)
    catalog.add(magazin)


def dvd_qoshish(catalog):
    title = input("Nomi : ")
    director = input("Regisiyor : ")
    subject = input("Janr : ")

    dvd = DVD(title,director,subject = "Umumiy")
    catalog.add(dvd)

def qidirish(catalog):
    soz = input("Qidiruv so'zi : ")
    result = catalog.search(soz)

    if result:
        for kitob in result:
            print(kitob.get_info())

    else:
        print("Xech narsa topilmadi ! ")



def main():
     catalog = Catalog()

     while True:
         print("""
         ===== USTUDY KUTUBXONA (OOP) =====
         1. Kitob qo'shish
         2. Jurnal qo'shish
         3. DVD qo'shish
         4. Qidirish
         5. Hammasini ko'rsatish
         6. Saqlash
         7. Yuklash
         0. Chiqish
         Tanlang: 
         """)

         tanlov = input("Bo'limni tanlang : ")
         if tanlov == "1":
             kitob_qoshish(catalog)
         elif tanlov == "2":
             jurnal_qoshish(catalog)
         elif tanlov == "3":
             dvd_qoshish(catalog)
         elif tanlov == "4":
             qidirish(catalog)
         elif tanlov == "5":
             catalog.hammasi()
             print(f"Jami : {catalog.jami()} ta element ! ")

         elif tanlov == "6":
             catalog.saqla("catalog.txt")
         elif tanlov == "7":
             catalog.yukla("catalog.txt")

         elif tanlov == "0":
             print("Dastur tugadi Xayr  !")
             break
         else:
             print("Nomalum tanlov - bunday bo'lim yoq  !")


main()






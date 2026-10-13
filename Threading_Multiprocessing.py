import unittest
from Kutubxona_Oop_talqinida import Author, Book, Magazin, DVD, Catalog, kitob_qoshish


class KutubxonaTest(unittest.TestCase):

    def qiymat(self):
        self.name = Author("Abdulla Qodiriy ")
        self.kitob = Book("Otgan kunlar ", self.name, "roman ")
        self.jurnal = Magazin("Kun uzz ", 5)
        self.disk = DVD("Shum bola ", "Gafur Gulom", "kamediya")
        self.catalog = Catalog()


    def test_kitob_malumotlari(self):
        info = self.kitob.get_info()
        self.assertIn("Otgan kunlar ",info)
        self.assertIn("Abdulla Qodiriy ", info)


    def test_jurnal_malumot(self):
        info = self.jurnal.get_info()
        self.assertIn("Kun uzz ", info)


    def test_dvd_malumot(self):
        info = self.disk.get_info()
        self.assertIn("Shum bola ", info)
        self.assertIn("Gafur Gulom", info)
        self.assertIn("kamediya", info)


    def test_katalog_qoshish(self):
        self.catalog.add(self.kitob)
        self.assertEqual(self.catalog.jami(), 1)

    def test_qidiruv(self):
        self.catalog.add(self.kitob)
        natija = self.catalog.search("Otgan kunlar ")
        self.assertEqual(len(natija), 1)


    def test_topilmadi(self):
        self.catalog.add(self.kitob)
        natija = self.catalog.search("Mexrobdan chayon ")
        self.assertEqual(len(natija), 0)


    def test_harflar_katta_kichik(self):
        self.catalog.add(self.disk)

        natija1 = self.catalog.search("SHUM")
        natija2 = self.catalog.search("shum")

        self.assertEqual(len(natija1), 1)
        self.assertEqual(len(natija2), 1)


    def test_jami(self):
        self.catalog.add(self.kitob)
        self.catalog.add(self.jurnal)
        self.catalog.add(self.disk)

        self.assertEqual(len(self.catalog.jami()), 3)


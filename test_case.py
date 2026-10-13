import unittest
from UNITEST import chegirma

class ChegirmaTest(unittest.TestCase):

    def test_oddiy(self):
        self.assertEqual(chegirma(100, 10), 90)

    def test_nol_foiz(self):
        self.assertEqual(chegirma(250, 0), 250)

    def test_yuz_foiz(self):
        self.assertEqual(chegirma(80, 100), 0)

    def test_notogri_foiz(self):
        with self.assertRaises(ValueError):
            chegirma(100, 150)


import unittest

from ..Konto import Konto

class TestCreateBankAccount(unittest.TestCase):
    def test_przelew_przychodzacy(self):
        konto9=Konto("Dariusz", "Januszewski", "12345678999")
        konto9.saldo=500
        konto9.zaksieguj_przelew_przychodzacy(100)
        self.assertEqual(konto9.saldo, 500 + 100, "Nie udało się wykonać operacji!")

    def test_przelew_wychodzacy_wystarczajace_srodki(self):
        konto8=Konto("Dariusz", "Januszewski", "12345678999")
        konto8.saldo=500
        konto8.zaksieguj_przelew_wychodzacy(100)
        self.assertEqual(konto8.saldo, 500 - 100, "Nie udało się wykonać operacji!")

    def test_przelew_wychodzacy_niewystarczajace_srodki(self):
        konto10=Konto("Dariusz", "Januszewski", "12345678999")
        konto10.saldo=50
        konto10.zaksieguj_przelew_wychodzacy(100)
        #self.assertEqual(konto10.saldo, 50 - 100, "Nie ma wystarczająco środków!")

    def test_seria_przelewow(self):
        konto11=Konto("Dariusz", "Januszewski", "12345678999")
        konto11.saldo=600
        konto11.zaksieguj_przelew_wychodzacy(100)
        konto11.zaksieguj_przelew_przychodzacy(200)
        self.assertEqual(konto11.saldo, 600-100+200, "Nie udało się wykonać operacji!")
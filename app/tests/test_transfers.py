import unittest

from ..KontoOsobiste import KontoOsobiste

class TestCreateBankAccount(unittest.TestCase):
    def test_przelew_przychodzacy(self):
        konto9=KontoOsobiste("Dariusz", "Januszewski", "12345678999")
        konto9.saldo=500
        konto9.zaksieguj_przelew_przychodzacy(100)
        self.assertEqual(konto9.saldo, 500 + 100, "Nie udało się wykonać operacji!")

    def test_przelew_wychodzacy_wystarczajace_srodki(self):
        konto8=KontoOsobiste("Dariusz", "Januszewski", "12345678999")
        konto8.saldo=500
        konto8.zaksieguj_przelew_wychodzacy(100)
        self.assertEqual(konto8.saldo, 500 - 100, "Nie udało się wykonać operacji!")

    def test_przelew_wychodzacy_niewystarczajace_srodki(self):
        konto10=KontoOsobiste("Dariusz", "Januszewski", "12345678999")
        konto10.saldo=50
        konto10.zaksieguj_przelew_wychodzacy(100)
        self.assertEqual(konto10.saldo, 50 , "Przy niewystarczajacych srodkach powinno zostac tyle samo co wczesniej!")

    def test_seria_przelewow(self):
        konto11=KontoOsobiste("Dariusz", "Januszewski", "12345678999")
        konto11.saldo=600
        konto11.zaksieguj_przelew_wychodzacy(100)
        konto11.zaksieguj_przelew_przychodzacy(200)
        self.assertEqual(konto11.saldo, 600-100+200, "Nie udało się wykonać operacji!")

    def test_przelew_ekspresowy(self):
        konto12=KontoOsobiste("Dariusz", "Januszewski", "12345678999")
        konto12.saldo=600
        konto12.przelew_ekspresowy(100)
        self.assertEqual(konto12.saldo, 600-100-1, "Nie udało się wykonać przelewu ekspresowego!")

    def test_przelew_ekspresowy_minus(self):
        konto12=KontoOsobiste("Dariusz", "Januszewski", "12345678999")
        konto12.saldo=100
        konto12.przelew_ekspresowy(100)
        self.assertEqual(konto12.saldo, 100-100-1, "Nie udało się wykonać przelewu ekspresowego!")
    
    def test_przelew_ekspresowy_blad(self):
        konto12=KontoOsobiste("Dariusz", "Januszewski", "12345678999")
        konto12.saldo=50
        konto12.przelew_ekspresowy(100)
        self.assertEqual(konto12.saldo, 50, "Przy nieudanym przelewie powinno wynosic 50!")
        

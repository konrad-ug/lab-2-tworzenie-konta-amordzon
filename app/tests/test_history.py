import unittest

from ..KontoOsobiste import KontoOsobiste
from ..KontoFirmowe import KontoFirmowe

class TestHistory(unittest.TestCase):
    def test_przelew_prywatne(self):
        konto=KontoOsobiste("Dariusz", "Januszewski", "12345678999")
        konto.saldo=500
        konto.zaksieguj_przelew_wychodzacy(100)
        konto.zaksieguj_przelew_wychodzacy(200)
        konto.zaksieguj_przelew_przychodzacy(100)
        self.assertEqual(konto.historia, [-100,-200,100], "Niepoprawna historia!")
    
    def test_przelew_prywatne_ekspresowy(self):
        konto=KontoOsobiste("Dariusz", "Januszewski", "12345678999")
        konto.saldo=500
        konto.zaksieguj_przelew_wychodzacy(100)
        konto.zaksieguj_przelew_wychodzacy(200)
        konto.zaksieguj_przelew_przychodzacy(100)
        konto.przelew_ekspresowy(100)
        self.assertEqual(konto.historia, [-100,-200,100, -100, -1], "Niepoprawna historia!")

    def test_przelew_firmowe(self):
        szoste_konto=KontoFirmowe("Firma", "123456789")
        szoste_konto.saldo=600
        szoste_konto.zaksieguj_przelew_wychodzacy(100)
        szoste_konto.zaksieguj_przelew_przychodzacy(200)
        self.assertEqual(szoste_konto.historia, [-100,200], "Niepoprawna historia!")

    def test_przelew_firmowe_ekspresowe(self):
        szoste_konto=KontoFirmowe("Firma", "123456789")
        szoste_konto.saldo=600
        szoste_konto.zaksieguj_przelew_wychodzacy(100)
        szoste_konto.zaksieguj_przelew_przychodzacy(200)
        szoste_konto.przelew_ekspresowy(100)
        self.assertEqual(szoste_konto.historia, [-100,200, -100, -5], "Niepoprawna historia!")
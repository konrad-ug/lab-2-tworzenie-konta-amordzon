import unittest

from ..KontoFirmowe import KontoFirmowe

class TestCreateBankAccount(unittest.TestCase):

    def test_tworzenie_konta_poprawnyNIP(self):
        pierwsze_konto = KontoFirmowe("Firma", "1234567899")
        self.assertEqual(pierwsze_konto.NIP, "Niepoprawny NIP!", "Udało się utworzyć konto")
    
    def test_tworzenie_konta_niepoprawnyNIP(self):
        drugie_konto = KontoFirmowe("Firma", "123456789")
        self.assertEqual(drugie_konto.NIP, "123456789", "Nie udało się utworzyć konta!")
    
    def test_przelew_wychodzacy_wystarczajace_srodki(self):
        trzecie_konto = KontoFirmowe("Firma", "123456789")
        trzecie_konto.saldo=500
        trzecie_konto.zaksieguj_przelew_wychodzacy(100)
        self.assertEqual(trzecie_konto.saldo, 500 - 100, "Nie udało się wykonać operacji!")

    def test_przelew_przychodzacy(self):
        czwarte_konto = KontoFirmowe("Firma", "123456789")
        czwarte_konto.saldo=500
        czwarte_konto.zaksieguj_przelew_przychodzacy(100)
        self.assertEqual(czwarte_konto.saldo, 500 + 100, "Nie udało się wykonać operacji!")

    def test_przelew_wychodzacy_niewystarczajace_srodki(self):
        piate_konto = KontoFirmowe("Firma", "123456789")
        piate_konto.saldo=50
        piate_konto.zaksieguj_przelew_wychodzacy(100)
        self.assertEqual(piate_konto.saldo, 50 - 100, "Nie ma wystarczająco środków!")

    def test_seria_przelewow(self):
        szoste_konto=KontoFirmowe("Firma", "123456789")
        szoste_konto.saldo=600
        szoste_konto.zaksieguj_przelew_wychodzacy(100)
        szoste_konto.zaksieguj_przelew_przychodzacy(200)
        self.assertEqual(szoste_konto.saldo, 600-100+200, "Nie udało się wykonać operacji!")
    
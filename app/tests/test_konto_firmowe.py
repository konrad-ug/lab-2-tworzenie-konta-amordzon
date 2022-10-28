import unittest

from ..KontoFirmowe import KontoFirmowe

class TestCreateBankAccount(unittest.TestCase):

    def test_tworzenie_konta_poprawnyNIP(self):
        pierwsze_konto = KontoFirmowe("Firma", "1234567899")
        self.assertEqual(pierwsze_konto.NIP, "Niepoprawny NIP!", "Udało się utworzyć konto")
    
    def test_tworzenie_konta_niepoprawnyNIP(self):
        drugie_konto = KontoFirmowe("Firma", "123456789")
        self.assertEqual(drugie_konto.NIP, "123456789", "Nie udało się utworzyć konta!")
    
    def test_przelew_wychodzacy(self):
        trzecie_konto = KontoFirmowe("Firma", "123456789")
        trzecie_konto.saldo=500
        trzecie_konto.zaksieguj_przelew_wychodzacy(100)
        self.assertEqual(trzecie_konto.saldo, 500 - 100, "Nie udało się wykonać operacji!")
    
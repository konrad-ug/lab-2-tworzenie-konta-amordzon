import unittest

from ..KontoFirmowe import KontoFirmowe

class TestCreateBankAccount(unittest.TestCase):

    def test_tworzenie_konta_poprawnyNIP(self):
        pierwsze_konto = KontoFirmowe("Firma", "1234567899")
        self.assertEqual(pierwsze_konto.NIP, "1234567899", "NIP nie zostal zapisany")
    
    def test_tworzenie_konta_niepoprawnyNIP(self):
        drugie_konto = KontoFirmowe("Firma", "123456789")
        self.assertEqual(drugie_konto.NIP, "Niepoprawny NIP!", "Przy podaniu niepoprawnego nipu wartosc nip powinna wynosic niepprawny nip")
    
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
        self.assertEqual(piate_konto.saldo, 50, "Przy niewystarczjacej ilosci srodkow kwota powinna zostac taka sama!")

    def test_seria_przelewow(self):
        szoste_konto=KontoFirmowe("Firma", "123456789")
        szoste_konto.saldo=600
        szoste_konto.zaksieguj_przelew_wychodzacy(100)
        szoste_konto.zaksieguj_przelew_przychodzacy(200)
        self.assertEqual(szoste_konto.saldo, 600-100+200, "Nie udało się wykonać operacji!")
    
    def test_przelew_ekspresowy(self):
        siodme_konto=KontoFirmowe("Firma", "123456789")
        siodme_konto.saldo=600
        siodme_konto.przelew_ekspresowy(100)
        self.assertEqual(siodme_konto.saldo, 600-100-5, "Nie udało się wykonać przelewu ekspresowego!")

    def test_przelew_ekspresowy_minus(self):
        osme_konto=KontoFirmowe("Firma", "123456789")
        osme_konto.saldo=100
        osme_konto.przelew_ekspresowy(100)
        self.assertEqual(osme_konto.saldo, 100-100-5, "Nie udało się wykonać przelewu ekspresowego!")
    
    def test_przelew_ekspresowy_blad(self):
        dziewiate_konto=KontoFirmowe("Firma", "123456789")
        dziewiate_konto.saldo=50
        dziewiate_konto.przelew_ekspresowy(100)
        self.assertEqual(dziewiate_konto.saldo, 50, "Przy nieudanym przelewie kwota powinna zostac taka sama!")
    
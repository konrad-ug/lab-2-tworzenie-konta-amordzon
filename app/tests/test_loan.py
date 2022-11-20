import unittest

from ..KontoOsobiste import KontoOsobiste

class TestLoan(unittest.TestCase):
    def test_loan_dobrze(self):
        konto=KontoOsobiste("Dariusz", "Januszewski", "12345678999")
        konto.saldo=1100
        konto.historia=[100,200,300,400,100]
        self.assertEqual(konto.zaciagnij_kredyt(200), True, "Nie udało się zaciágnąć kredytu!")
        self.assertEqual(konto.saldo, 1300, "Niepoprawna kwota!")
    
    def test_loan_za_malo_przelewow(self):
        konto=KontoOsobiste("Dariusz", "Januszewski", "12345678999")
        konto.saldo=1100
        konto.historia=[100,200]
        self.assertEqual(konto.zaciagnij_kredyt(200), False, "W przypadku za malej ilosci przelewow powinien być błąd!")
        self.assertEqual(konto.saldo, 1100, "Niepoprawna kwota!")
    
    def test_loan_przelew_wyplata(self):
        konto=KontoOsobiste("Dariusz", "Januszewski", "12345678999")
        konto.saldo=1100
        konto.historia=[-100,200,300,400,100]
        self.assertEqual(konto.zaciagnij_kredyt(200), False, "W przypadku wyplaty kredyt nie powinien byc moc zaciagniety!")
        self.assertEqual(konto.saldo, 1100, "Niepoprawna kwota!")
    
    def test_loan_za_duzy_kredyt(self):
        konto=KontoOsobiste("Dariusz", "Januszewski", "12345678999")
        konto.saldo=1100
        konto.historia=[100,200,300,400,100]
        self.assertEqual(konto.zaciagnij_kredyt(20000), False,  "W przypadku kiedy kredyt jest za duzy powinien byc blad!")
        self.assertEqual(konto.saldo, 1100, "Niepoprawna kwota!")



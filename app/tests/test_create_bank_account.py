import unittest

from ..KontoOsobiste import KontoOsobiste

class TestCreateBankAccount(unittest.TestCase):

    def test_tworzenie_konta(self):
        pierwsze_konto = KontoOsobiste("Dariusz", "Januszewski", "12345678999")
        self.assertEqual(pierwsze_konto.imie, "Dariusz", "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, "Januszewski", "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")


        self.assertEqual(pierwsze_konto.pesel, "12345678999", "Pesel nie został zapisany!")

        #pesel

        self.assertEqual(len(pierwsze_konto.pesel), 11, "Nieprawidłowa długość peselu")

        drugie_konto = KontoOsobiste("Dariuszdwa", "Januszewskidwa", "122256789ab")
        self.assertEqual(drugie_konto.pesel, "Niepoprawny pesel!", "Pesel nie ma wartości Niepoprawny pesel! jeżeli jest zły")

    def test_kod(self):
        #kod
        trzecie_konto= KontoOsobiste("Dariusztrzy", "Januszewskitrzy", "12325678999", "PROM_ABC")

        czwarte_konto= KontoOsobiste("Dariuszcztery", "Januszewskicztery", "12345678999", "PRddddM_ABC")

    def test_pesel(self):
        #pesel
        piate_konto= KontoOsobiste("Dariuszcztery", "Januszewskicztery", "44045678999", "PROM_ABC")
        self.assertEqual(piate_konto.saldo, 0, "Saldo powinno sie rownac 0 dla osob z dobrym kodem i urodzonych przed 1960!")

        piate_konto= KontoOsobiste("Dariuszpiec", "Januszewskipiec", "02315678999", "PROM_ABC")
        self.assertEqual(piate_konto.saldo, 50, "Saldo powinno sie rownac 50 dla osob z dobrym kodem i urodzonych po 1960!")

        
        szoste_konto= KontoOsobiste("Dariuszszesc", "Januszewskiszesc", "02315678999", "PROMs_ABC")
        self.assertEqual(szoste_konto.saldo, 0, "Saldo powinno sie rownac 0 dla osob ze zlym kodem i urodzonych po 1960!")

        
        siodme_konto= KontoOsobiste("Dariuszsiedem", "Januszewskisiedem", "44045678999", "PROMs_ABC")
        self.assertEqual(siodme_konto.saldo, 0, "Saldo powinno sie rownac 0 dla osob ze zlym kodem i urodzonych przed 1960!")

    #tutaj proszę dodawać nowe testy
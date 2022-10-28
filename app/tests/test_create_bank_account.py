import unittest

from ..Konto import Konto

class TestCreateBankAccount(unittest.TestCase):

    def test_tworzenie_konta(self):
        pierwsze_konto = Konto("Dariusz", "Januszewski", "12345678999")
        self.assertEqual(pierwsze_konto.imie, "Dariusz", "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, "Januszewski", "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")


        self.assertEqual(pierwsze_konto.pesel, "12345678999", "Pesel nie został zapisany!")

        #pesel

        self.assertEqual(len(pierwsze_konto.pesel), 11, "Nieprawidłowa długość peselu")

        drugie_konto= Konto("Dariuszdwa", "Januszewskidwa", "12345678999")
        #self.assertEqual(drugie_konto.pesel, "Niepoprawny pesel!", "Pesel jest poprawny!")

    def test_kod(self):
        #kod
        trzecie_konto= Konto("Dariusztrzy", "Januszewskitrzy", "12325678999", "PROM_ABC")
        self.assertEqual(trzecie_konto.saldo, 50, "Bledny kod promocyjny!")

        czwarte_konto= Konto("Dariuszcztery", "Januszewskicztery", "12345678999", "PRddddM_ABC")
        self.assertEqual(czwarte_konto.saldo, 0, "W przypadku błędnego kodu, saldo powinno się równać 0!")

    def test_pesel(self):
        #pesel
        piate_konto= Konto("Dariuszcztery", "Januszewskicztery", "44045678999", "PROM_ABC")
        self.assertEqual(piate_konto.saldo, 0, "Saldo powinno sie rownac 0 dla osob z dobrym kodem i urodzonych przed 1960!")

        piate_konto= Konto("Dariuszpiec", "Januszewskipiec", "02315678999", "PROM_ABC")
        self.assertEqual(piate_konto.saldo, 50, "Saldo powinno sie rownac 50 dla osob z dobrym kodem i urodzonych po 1960!")

        
        szoste_konto= Konto("Dariuszszesc", "Januszewskiszesc", "02315678999", "PROMs_ABC")
        self.assertEqual(szoste_konto.saldo, 0, "Saldo powinno sie rownac 0 dla osob ze zlym kodem i urodzonych po 1960!")

        
        siodme_konto= Konto("Dariuszsiedem", "Januszewskisiedem", "44045678999", "PROMs_ABC")
        self.assertEqual(siodme_konto.saldo, 0, "Saldo powinno sie rownac 0 dla osob ze zlym kodem i urodzonych przed 1960!")

    #tutaj proszę dodawać nowe testy
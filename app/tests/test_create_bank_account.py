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
        self.assertEqual(len(drugie_konto.pesel), "Niepoprawny pesel!", "Pesel jest poprawny!")

        #kod



    #tutaj proszę dodawać nowe testy
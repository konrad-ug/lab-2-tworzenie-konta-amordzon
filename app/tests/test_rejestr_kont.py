import unittest

from ..KontoOsobiste import KontoOsobiste
from ..RejestrKont import RejestrKont

class TestRejestrKont(unittest.TestCase):
    imie="darek"
    nazwisko="Januszewski"
    pesel="12345678999"

    @classmethod
    def setUpClass(cls):
        konto=KontoOsobiste(cls.imie, cls.nazwisko, cls.pesel)
        RejestrKont.addAccountToArray(konto)

    def test_1_dodanie_pierwszego_konta(self):
        konto=KontoOsobiste(self.imie, self.nazwisko, self.pesel)
        RejestrKont.addAccountToArray(konto)
        self.assertEqual(RejestrKont.accountLength(),2, "Tylko jedno konto powinno byc")
    
    def test_1_dodanie_pierwszego_konta(self):
        konto=KontoOsobiste(self.imie, self.nazwisko, self.pesel)
        konto2=KontoOsobiste(self.imie+"ddd", self.nazwisko, self.pesel)
        RejestrKont.addAccountToArray(konto)
        RejestrKont.addAccountToArray(konto2)
        self.assertEqual(RejestrKont.accountLength(),3, "Powinny byc 2 konta")
    
    def test_znajdz_konto(self):
        konto=KontoOsobiste(self.imie, self.nazwisko, self.pesel)
        konto2=KontoOsobiste(self.imie+"ddd", self.nazwisko, "12345678997")
        RejestrKont.addAccountToArray(konto)
        RejestrKont.addAccountToArray(konto2)
        self.assertEqual(RejestrKont.findByPesel("12345678997"),konto2, "Drugie konto powinno byc znaleznione")
    
    @classmethod
    def tearDownClass(cls):
        RejestrKont.usersAccounts=[]


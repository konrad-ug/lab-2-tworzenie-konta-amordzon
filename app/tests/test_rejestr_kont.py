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
        konto2=KontoOsobiste(self.imie+"ddd", self.nazwisko, self.pesel)
        RejestrKont.addAccountToArray(konto)
        RejestrKont.addAccountToArray(konto2)
        self.assertEqual(RejestrKont.accountLength(),3, "Powinny byc 3 konta")
    
    def test_2_dodanie_drugiego_konta(self):
        konto=KontoOsobiste(self.imie, self.nazwisko, self.pesel)
        RejestrKont.addAccountToArray(konto)
        self.assertEqual(RejestrKont.accountLength(),4, "Powinny byc 4 konta")
    

    def test_3_znajdz_konto(self):
        konto=KontoOsobiste(self.imie, self.nazwisko, self.pesel)
        konto2=KontoOsobiste(self.imie+"ddd", self.nazwisko, "12345678997")
        RejestrKont.addAccountToArray(konto)
        RejestrKont.addAccountToArray(konto2)
        self.assertEqual(RejestrKont.findByPesel("12345678997"),konto2, "Drugie konto powinno byc znaleznione")

    def test_4_znajdz_konto(self):
        konto=KontoOsobiste(self.imie, self.nazwisko, self.pesel)
        konto2=KontoOsobiste(self.imie+"ddd", self.nazwisko, "12345668997")
        konto3=KontoOsobiste(self.imie+"ddd", self.nazwisko, "12345668997")
        RejestrKont.addAccountToArray(konto)
        RejestrKont.addAccountToArray(konto2)
        RejestrKont.addAccountToArray(konto3)
        self.assertEqual(RejestrKont.findByPesel("12345668997"),konto2, "Drugie konto powinno byc znaleznione")
    
    def test_5_znajdz_konto_nie_ma(self):
        self.assertEqual(RejestrKont.findByPesel("12444678997"),None, "None powinno byc zwrocone")
    
    @classmethod
    def tearDownClass(cls):
        RejestrKont.usersAccounts=[]


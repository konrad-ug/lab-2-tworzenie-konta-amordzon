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
        konto = KontoOsobiste(self.imie, self.nazwisko, "22335678999")
        konto2 = KontoOsobiste(self.imie+"ddd", self.nazwisko, "22345678999")
        RejestrKont.addAccountToArray(konto)
        RejestrKont.addAccountToArray(konto2)
        self.assertEqual(RejestrKont.accountLength(),3, "Powinny byc 3 konta")
    
    def test_2_dodanie_drugiego_konta(self):
        konto = KontoOsobiste(self.imie, self.nazwisko, "32335678999")
        RejestrKont.addAccountToArray(konto)
        self.assertEqual(RejestrKont.accountLength(),4, "Powinny byc 4 konta")
    

    def test_3_znajdz_konto(self):
        konto = KontoOsobiste(self.imie, self.nazwisko, "92335678999")
        konto2=KontoOsobiste(self.imie+"ddd", self.nazwisko, "12345678997")
        RejestrKont.addAccountToArray(konto)
        RejestrKont.addAccountToArray(konto2)
        self.assertEqual(RejestrKont.findByPesel("12345678997"),konto2, "Drugie konto powinno byc znaleznione")

    def test_4_znajdz_konto(self):
        konto = KontoOsobiste(self.imie, self.nazwisko, "99345668997")
        konto2=KontoOsobiste(self.imie+"ddd", self.nazwisko, "12345668997")
        konto3=KontoOsobiste(self.imie+"ddd", self.nazwisko, "12345668997")
        RejestrKont.addAccountToArray(konto)
        RejestrKont.addAccountToArray(konto2)
        RejestrKont.addAccountToArray(konto3)
        self.assertEqual(RejestrKont.findByPesel("12345668997"),konto2, "Drugie konto powinno byc znaleznione")
    
    def test_5_znajdz_konto_nie_ma(self):
        self.assertEqual(RejestrKont.findByPesel("12444678997"),None, "None powinno byc zwrocone")
    

    def test_6_usun_konto_ok(self):
        account_len=RejestrKont.accountLength()
        self.assertEqual(RejestrKont.accountRemove(
            "12345678999"), "User deleted", "Uzytkownik nie zostal usuniety")
        self.assertEqual(RejestrKont.accountLength(), account_len - 1)
    
    def test_7_usun_konto_nie_ma(self):
        account_len = RejestrKont.accountLength()
        self.assertEqual(RejestrKont.accountRemove(
            "12345678991"), None, "None powinno byc zwrocone")
        self.assertEqual(RejestrKont.accountLength(), account_len)

    def test_8_aktualizuj_konto_ok(self):
        konto = KontoOsobiste("test", "testtt", "22225668997")
        RejestrKont.addAccountToArray(konto)
        update = {
            "imie": "git",
            "nazwisko": "nazwiskooo",
            "saldo": 1
        }
        self.assertEqual(RejestrKont.accountUpdate(
            "22225668997", update), RejestrKont.findByPesel("22225668997"), "Konto nie zostalo zaktualizowane")
    
    def test_9_aktualizuj_konto_zle(self):
        konto = KontoOsobiste("testkolejny", "testttyyy", "22225669997")
        RejestrKont.addAccountToArray(konto)
        update = {
            "imie": "git",
            "nazwisko": "nazwiskooo",
            "saldo": 1
        }
        self.assertEqual(RejestrKont.accountUpdate(
            "22222228997", update), None, "None powinno zostac zwrocone w przypadku gdy pesel nie istnieje")

    @classmethod
    def tearDownClass(cls):
        RejestrKont.usersAccounts=[]


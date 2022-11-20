import unittest

from ..KontoFirmowe import KontoFirmowe
from parameterized import parameterized

class TestLoanCompany(unittest.TestCase):
    def setUp(self):
        self.konto=KontoFirmowe("Firma", "123456789")

    @parameterized.expand([
        ([100,200,300,400,100, -1775], 200, 100, True, 300),
        ([-1775,100,200,300,400,100, -1775], 200, 100, True, 300),
        ([100,200], 500, 200, False, 500),
        ([100,200, 1775], 500, 200, False, 500),
        ([-100,200,300,400,100, -1775], 100, 100, False, 100),
    ])

    def test_loan(self, historia, saldo, kwota, oczek_wyn, oczek_saldo):
        self.konto.historia=historia
        self.konto.saldo=saldo
        self.assertEqual(self.konto.zaciagnij_kredyt(kwota), oczek_wyn, "Nie udało się zaciágnąć kredytu!")
        self.assertEqual(self.konto.saldo, oczek_saldo, "Niepoprawna kwota!")
    



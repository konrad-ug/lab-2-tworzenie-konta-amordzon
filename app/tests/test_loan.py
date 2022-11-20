import unittest

from ..KontoOsobiste import KontoOsobiste
from parameterized import parameterized

class TestLoan(unittest.TestCase):
    def setUp(self):
        self.konto=KontoOsobiste("Dariusz", "Januszewski", "12345678999")

    @parameterized.expand([
        ([100,200,300,400,100], 100, True, 100),
        ([100,200], 100, False, 0),
        ([-100,200,300,400,100], 100, False, 0),
        ([100,200,300,400,100], 3000, False, 0),
        ([100,200,300,400,100,-600], 300, True, 300),
    ])

    def test_loan(self, historia, kwota, oczek_wyn, oczek_saldo):
        self.konto.historia=historia
        self.assertEqual(self.konto.zaciagnij_kredyt(kwota), oczek_wyn, "Nie udało się zaciágnąć kredytu!")
        self.assertEqual(self.konto.saldo, oczek_saldo, "Niepoprawna kwota!")
    



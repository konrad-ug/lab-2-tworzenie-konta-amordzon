from .Konto import Konto

class KontoFirmowe(Konto):
    def __init__(self, nazwa, NIP):
        self.nazwa = nazwa
        self.saldo = 0
        self.validateNIP(NIP)

    def validateNIP(self, NIP):
        if(len(NIP)==10 and NIP.isdigit()):
            self.NIP=NIP
        else:
            self.NIP="Niepoprawny NIP!"

    def przelew_ekspresowy(self, kwota):
        super().przelew_ekspresowy(kwota,5)

    
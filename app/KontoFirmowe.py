from .Konto import Konto

class KontoFirmowe(Konto):
    def __init__(self, nazwa, NIP):
        self.nazwa = nazwa
        self.saldo = 0
        self.validateNIP(NIP)

    def validateNIP(self, NIP):
        if(len(NIP)==10):
            self.NIP=NIP
        else:
            self.NIP="Niepoprawny NIP!"

    
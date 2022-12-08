from .Konto import Konto

class KontoFirmowe(Konto):
    def __init__(self, nazwa, NIP):
        super().__init__()
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

    def zaciagnij_kredyt(self, kwota):
        if(len(self.historia)>0 and self.saldo>=kwota*2 and -1775 in self.historia):
            self.saldo+=kwota
            return True
        return False

from .Konto import Konto

class KontoOsobiste(Konto):
    def __init__(self, imie, nazwisko, pesel, prom=None):
        super().__init__()
        self.imie = imie
        self.nazwisko = nazwisko
        self.saldo = 0
        self.check_pesel(pesel)
        self.check_prom(prom)

    def check_pesel(self,pesel):
        if(len(pesel)!=11 or not pesel.isdigit()):
            self.pesel="Niepoprawny pesel!"
        else:
            self.pesel=pesel
    
    def check_prom(self, prom):
        if(prom!=None and prom.startswith('PROM_') and len(prom)==8 and ( int(self.pesel[:2])>60 or (int(self.pesel[2:4])>20 and int(self.pesel[2:4])<33))):
            self.saldo=50

    def przelew_ekspresowy(self, kwota):
        super().przelew_ekspresowy(kwota, 1)
    
    def zaciagnij_kredyt(self, kwota):
        if(len(self.historia)>=5 and all([x > 0 for x in self.historia[:3]]) and sum(self.historia[:5])>kwota):
            self.saldo+=kwota
            return True
        return False
    

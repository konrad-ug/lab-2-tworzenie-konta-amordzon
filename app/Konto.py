class Konto:
    def __init__(self, imie, nazwisko, pesel, prom=None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.saldo = 0
        self.check_pesel(pesel)
        self.check_prom(prom)

    def check_pesel(self,pesel):
        if(len(pesel)!=11):
            self.pesel="Niepoprawny pesel!"
        else:
            self.pesel=pesel
    
    def check_prom(self, prom):
        if(prom!=None and prom.startswith('PROM_') and len(prom)==8 and ( int(self.pesel[:2])>60 or int(self.pesel[2:4])>12)):
            self.saldo=50

    

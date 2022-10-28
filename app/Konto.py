class Konto:
    def __init__(self, imie, nazwisko, pesel, saldo, prom=None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.saldo = saldo
        self.check_pesel(pesel)
        self.check_prom(prom)

    def check_pesel(self,pesel):
        if(len(pesel)!=11 or not pesel.isnumeric()):
            self.pesel="Niepoprawny pesel!"
        else:
            self.pesel=pesel
    
    def check_prom(self, prom):
        if(prom!=None and prom.startswith('PROM_') and len(prom)==8 and ( int(self.pesel[:2])>60 or (int(self.pesel[2:4])>20 and int(self.pesel[2:4])<33))):
            self.saldo=50
    
    def zaksieguj_przelew_wychodzacy(self,ile):
        if(self.saldo-ile>=0):
            self.saldo-=ile

    def zaksieguj_przelew_przychodzacy(self, ile):
        self.saldo+=ile
    

class Konto:
    def __init__(self, imie, nazwisko, pesel):
        self.imie = imie
        self.nazwisko = nazwisko
        self.saldo = 0
        self.check_pesel(pesel)

    def check_pesel(self,pesel):
        if(len(pesel)!=11):
            self.pesel="Niepoprawny pesel!"
        else:
            self.pesel=pesel
    

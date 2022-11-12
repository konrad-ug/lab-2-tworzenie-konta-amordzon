class Konto:
    def __init__(self):
        self.historia=[]
    
    def zaksieguj_przelew_wychodzacy(self,ile):
        if(self.saldo-ile>=0):
            self.saldo-=ile
        self.historia.append(ile*-1) 

    def zaksieguj_przelew_przychodzacy(self, ile):
        self.saldo+=ile
        self.historia.append(ile) 

    def przelew_ekspresowy(self, kwota, oplata):
        if(self.saldo >= kwota):
            self.saldo -= (kwota + oplata)
            self.historia.append(kwota*-1)
            self.historia.append(oplata*-1)  
        else:
            self.saldo = self.saldo
    

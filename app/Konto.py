class Konto:
    
    def zaksieguj_przelew_wychodzacy(self,ile):
        if(self.saldo-ile>=0):
            self.saldo-=ile

    def zaksieguj_przelew_przychodzacy(self, ile):
        self.saldo+=ile

    def przelew_ekspresowy(self, kwota, oplata=1):
        if(self.saldo - kwota - oplata >= -oplata):
            self.saldo -= (kwota + oplata)
        else:
            self.saldo = self.saldo
    

class RejestrKont:
    usersAccounts=[]
    
    @classmethod
    def addAccountToArray(cls, account):
        cls.usersAccounts.append(account)
    
    @classmethod
    def findByPesel(cls, pesel):
        return next((x for x in cls.usersAccounts if x.pesel == pesel), None)
    
    @classmethod
    def accountLength(cls):
        return len(cls.usersAccounts)

    @classmethod
    def accountUpdate(cls, pesel, dane):
        if(cls.findByPesel(pesel) != None):
            konto=cls.findByPesel(pesel)
            konto.imie=dane["imie"] if "imie" in dane else konto.imie
            konto.nazwisko=dane["nazwisko"] if "nazwisko" in dane else konto.nazwisko
            konto.pesel=dane["pesel"] if "pesel" in dane else konto.pesel
            konto.saldo=dane["saldo"] if "saldo" in dane else konto.saldo
            return konto
        else:
            return None
    
    @classmethod
    def accountRemove(cls, pesel):
        if(cls.findByPesel(pesel) != None):
            cls.usersAccounts = [
                x for x in cls.usersAccounts if x.pesel != pesel]
            return "User deleted"
        else:
            return None

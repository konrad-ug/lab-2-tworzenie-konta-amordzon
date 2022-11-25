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

class RejestrKont:
    usersAccounts=[]
    
    @classmethod
    def addAccountToArray(self, account):
        self.usersAccounts.append(account)
    
    @classmethod
    def findByPesel(self, pesel):
        return next((x for x in self.usersAccounts if x.pesel == pesel), None)
    
    @classmethod
    def accountLength(self):
        return len(self.usersAccounts)

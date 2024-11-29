class Account:
    def __init__(self, number:int, holder:str,balance:float):
        self.number=number
        self.holder=holder
        self.balance=balance

    def withdraw(self,amount:float):
        if amount > 0 and amount<=self.balance:
        self.balance-=amount
            print ("Get the drift")
        else:
            print("insufficient balance")    

    def deposit(self, amount:float):
        if amount >0
        self.balance+=amount
        el
    

class BussinesAccount(Account):

    def __init__(self, number: int, holder: str, balance: float,loadlimit:float):
        super().__init__(number, holder, balance)
        self.loadlimit=loadlimit
              
    
    def loan(self, amount:float):
        if amount > 0 and amount<= self.loadlimit:
            self.balance+= amount
        else:
            print 




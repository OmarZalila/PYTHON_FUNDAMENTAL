class BankAccount:
    accounts=[]
    def __init__(self, int_rate, balance=0): 
        self.int_rate=int_rate
        self.balance=balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance+=amount
        return self
    
    def withdraw(self, amount):
        self.balance-=amount
        return self
    
    def display_account_info(self):
        print(f"balance : ${self.balance}")
    
    def yield_interest(self):
        if BankAccount.can_yield_interest(self.balance):
            self.balance+=self.balance*self.int_rate
        return self
        
    @staticmethod
    def can_yield_interest(balance):
        if balance > 0 :
            return True
        else :
            return False
    @classmethod
    def all_instances(cls):
        for account in cls.accounts:
            print(f"int_rate : {account.int_rate} , balance : {account.balance}")

person_1=BankAccount(0.02,100)
person_2=BankAccount(0.01,200)

BankAccount.all_instances()
person_1.deposit(20).deposit(20).deposit(20).withdraw(170).yield_interest().display_account_info()
person_2.deposit(20).deposit(20).withdraw(20).withdraw(20).withdraw(20).withdraw(20).yield_interest().display_account_info()                  
BankAccount.all_instances()
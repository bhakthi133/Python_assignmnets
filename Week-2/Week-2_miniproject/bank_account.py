class BankAccount:
    def __init__(self,account_number, holder_name,balance):
        self.acount_number=account_number
        self.holder_name=holder_name
        self._balance=balance
        self.transaction_history=[]

    def deposit(self,amount):
        if(amount<0):
            print("Invalid deposit")
            self.transaction_history.append({"Operation":"deposit","Amount":amount,"Status":"Failed","Balance":self._balance})
            return
        self._balance=self._balance+amount
        self.transaction_history.append({"Operation":"deposit","Amount":amount,"Status":"Success","Balance":self._balance})

    def withdraw(self,amount):
        if(amount<=0):
            print("Enter valid amount")
            self.transaction_history.append({"Operation":"Withdraw","Amount":amount,"Status":"Failed","Balance":self._balance})
            return
        if(self._balance>=amount):
            self._balance=self._balance-amount
            self.transaction_history.append({"Operation":"Withdraw","Amount":amount,"Status":"Success","Balance":self._balance})
        else:
            print("Invalid amount no suficent fund")
            self.transaction_history.append({"Operation":"Withdraw","Amount":amount,"Status":"Failed","Balance":self._balance})

    def get_balance(self):
        self.transaction_history.append({"Operation":"Check balance","Status":"Success","Balance":self._balance})
        return self._balance
        
class SavingsAccount(BankAccount):
    def __init__(self, account_number, holder_name, balance, interest_rate):
        super().__init__(account_number, holder_name, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        self._balance=self._balance+(self._balance*self.interest_rate/100)
        self.transaction_history.append({"Operation":"Intrest apply","Intrest":self._balance*self.interest_rate/100,"Status":"Succes","Balance":self._balance})
            
class CurrentAccount(BankAccount):
    def __init__(self, account_number, holder_name, balance, overdraft_limit):
        super().__init__(account_number,holder_name,balance)
        self.overdraft_limit=overdraft_limit
    def withdraw(self,amount):
            if(amount<=0):
                print("Enter valid amount")
                self.transaction_history.append({"Operation":"Withdraw","Amount":amount,"Status":"Failed","Balance":self._balance})
                return
            if(self._balance+self.overdraft_limit>=amount):
                self._balance=self._balance-amount
                self.transaction_history.append({"Operation":"Withdraw","Amount":amount,"Status":"Success","Balance":self._balance})
            else:
                print("Invalid amount no suficent fund")
                self.transaction_history.append({"Operation":"Withdraw","Amount":amount,"Status":"Failed","Balance":self._balance})



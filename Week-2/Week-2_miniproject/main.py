from bank_account import BankAccount,CurrentAccount,SavingsAccount

Saving1=SavingsAccount(12345,'abc',10056,5)
Saving2=SavingsAccount(67853,"ojkn",234,5)
Cur1=CurrentAccount(75325,"bhg",1780,987)

Saving1.deposit(-1)
Saving1.deposit(100)
Saving1.get_balance()
Saving1.withdraw(980678)
Saving1.apply_interest()
print(Saving1.transaction_history)

Cur1.deposit(-1)
Cur1.deposit(100)
Cur1.get_balance()
Cur1.withdraw(980678)

print(Saving1.transaction_history)



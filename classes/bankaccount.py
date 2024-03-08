class BankAccount:

    def init(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, sum_of_moneys):
        self.balance += sum_of_moneys

    def withdraw(self, sum_of_moneys):
        self.balance -= sum_of_moneys

    def check_balance(self):
        return self.balance


Dima = BankAccount("Dima", 10000)
Vlad = BankAccount("Vlad", 15000)
Anon = BankAccount("Anon", 5000)

Dima.deposit(5000)
Vlad.withdraw(5000)
Anon.withdraw(2000)
print(Dima.check_balance(), Vlad.check_balance(), Anon.check_balance(), sep='\n')

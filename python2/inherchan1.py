class Account:
    def __init__(self, title,balance):
        self.title = title
        self.balance = balance


class SavingsAccount(Account):
    def __init__(self, title, balance, interestRate):
        super().__init__(title, balance)
        self.interestRate = interestRate

details = SavingsAccount("Mark", 5000, 5)        
print(details.title)
print(details.balance)
print(details.interestRate)
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number=account_number
        self.balance= balance

    def deposit(self):
        x=int(input("type your account number{}".format(self.account_number)))
        y=int(input("depost your money {}".format(self.balance)))
        print(x,y)
customer=BankAccount(2425,200)
customer.deposit()


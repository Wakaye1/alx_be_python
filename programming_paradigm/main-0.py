# main-0.py

import sys
from bank_account import BankAccount

def main():
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <operation> [amount]")
        return

    operation = sys.argv[1]

    # Initialize the bank account with an optional initial balance
    account = BankAccount()

    if operation == 'deposit':
        if len(sys.argv) != 3:
            print("Usage: python main-0.py deposit <amount>")
            return
        amount = float(sys.argv[2])
        account.deposit(amount)
        print(f"Deposited ${amount:.2f}")

    elif operation == 'withdraw':
        if len(sys.argv) != 3:
            print("Usage: python main-0.py withdraw <amount>")
            return
        amount = float(sys.argv[2])
        if account.withdraw(amount):
            print(f"Withdrew ${amount:.2f}")
        else:
            print("Insufficient funds")

    elif operation == 'balance':
        account.display_balance()

    else:
        print("Unknown operation. Available operations: deposit, withdraw, balance")

if __name__ == "__main__":
    main()

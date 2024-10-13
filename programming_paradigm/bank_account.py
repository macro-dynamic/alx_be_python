class BankAccount:
    def __init__(self, initial_balance=0):
        """
        Initialize a BankAccount instance with an optional initial balance.
        """
        self.account_balance = initial_balance

    def deposit(self, amount):
        """
        Deposit the specified amount into the account.
        """
        self.account_balance += amount

    def withdraw(self, amount):
        """
        Withdraw the specified amount from the account if sufficient funds are available.
        Returns True if the withdrawal is successful, False otherwise.
        """
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        """
        Print the current account balance in a user-friendly format.
        """
        print(f"Current Balance: ${self.account_balance:.2f}")

import sys
from bank_account import BankAccount

def main():
    account = BankAccount(100)  # Example starting balance
    if len(sys.argv) < 2:
        print("Usage: python main.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount:.2f}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount:.2f}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()

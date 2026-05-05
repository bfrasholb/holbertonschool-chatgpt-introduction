#!/usr/bin/env python3.8

class Checkbook:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than 0.")
            return
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than 0.")
            return
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        print("Current Balance: ${:.2f}".format(self.balance))


def get_valid_amount(prompt):
    """Safely get a valid float amount from the user."""
    while True:
        user_input = input(prompt)
        try:
            amount = float(user_input)
            return amount
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")


def main():
    cb = Checkbook()

    while True:
        try:
            action = input(
                "What would you like to do? (deposit, withdraw, balance, exit): "
            ).strip().lower()

            if action == 'exit':
                print("Goodbye!")
                break

            elif action == 'deposit':
                amount = get_valid_amount("Enter the amount to deposit: $")
                cb.deposit(amount)

            elif action == 'withdraw':
                amount = get_valid_amount("Enter the amount to withdraw: $")
                cb.withdraw(amount)

            elif action == 'balance':
                cb.get_balance()

            else:
                print("Invalid command. Please try again.")

        except KeyboardInterrupt:
            print("\nExiting program.")
            break


if __name__ == "__main__":
    main()

#!/usr/bin/python3
class Checkbook:
    """
    A simple checkbook class for managing a balance with deposit, withdrawal,
    and balance inquiry functionalities.
    """

    def __init__(self):
        """
        Initialize the Checkbook with a starting balance of 0.0.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposit an amount into the checkbook.

        Parameters:
        amount (float): The amount to be deposited. Must be a positive number.

        Returns:
        None
        """
        if amount <= 0:
            print("Deposit amount must be greater than zero.")
            return
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraw an amount from the checkbook.

        Parameters:
        amount (float): The amount to be withdrawn. Must be a positive number
        and less than or equal to the current balance.

        Returns:
        None
        """
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        elif amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Display the current balance.

        Returns:
        None
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """
    Main function to interact with the Checkbook. Allows the user to deposit,
    withdraw, check balance, or exit the program.

    Returns:
    None
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()

        if action == 'exit':
            print("Thank you for using the Checkbook. Goodbye!")
            break
        elif action == 'deposit':
            while True:
                try:
                    deposit_input = input("Enter the amount to deposit: $").strip()

                    # Remove dollar sign and try converting to float
                    amount = float(deposit_input.replace('$', '').strip())
                    if amount <= 0:
                        print("Deposit amount must be greater than zero.")
                    else:
                        cb.deposit(amount)
                        break
                except ValueError:
                    print("Invalid input. Please enter a valid numeric value for the deposit amount.")
        elif action == 'withdraw':
            while True:
                try:
                    withdraw_input = input("Enter the amount to withdraw: $").strip()

                    # Remove dollar sign and try converting to float
                    amount = float(withdraw_input.replace('$', '').strip())
                    if amount <= 0:
                        print("Withdrawal amount must be greater than zero.")
                    elif amount > cb.balance:
                        print("Insufficient funds to complete the withdrawal.")
                    else:
                        cb.withdraw(amount)
                        break
                except ValueError:
                    print("Invalid input. Please enter a valid numeric value for the withdrawal amount.")
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
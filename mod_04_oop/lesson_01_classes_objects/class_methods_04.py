#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-201
# Lesson: Class Methods Example
#
# Description: This program demonstrates defining and using methods within a class.
#              The `BankAccount` class includes methods for depositing and
#              withdrawing money, allowing interaction with an account balance.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

def main():
    print("========== Methods in a Class: BankAccount Example ==========")
    print("This program demonstrates defining and using methods within a class.")
    print("*" * 80)

    # Create an instance of the BankAccount class for Alice
    alice_account = BankAccount("Alice")
    alice_account.display_balance()

    # Deposit and withdraw funds
    alice_account.deposit(100)  # Expected output: Deposited 100. New balance is 100.
    alice_account.withdraw(50)  # Expected output: Withdrew 50. New balance is 50.
    alice_account.withdraw(200) # Expected output: Insufficient funds!

    print("*" * 80)

# Define the BankAccount class
class BankAccount:
    """
    A simple BankAccount class to demonstrate methods.

    Attributes:
        account_holder (str): The name of the account holder.
        balance (float): The current balance in the account.
    """

    def __init__(self, account_holder, balance=0):
        """
        Initialize a new BankAccount instance.

        Args:
            account_holder (str): The name of the account holder.
            balance (float, optional): Initial balance. Defaults to 0.
        """
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        """
        Deposit a specified amount into the account.

        Args:
            amount (float): The amount to deposit.
        """
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}.")

    def withdraw(self, amount):
        """
        Withdraw a specified amount from the account if sufficient funds are available.

        Args:
            amount (float): The amount to withdraw.
        """
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")

    def display_balance(self):
        """
        Display the current balance of the account.
        """
        print(f"{self.account_holder}'s account balance is {self.balance}.")

if __name__ == "__main__":
    main()

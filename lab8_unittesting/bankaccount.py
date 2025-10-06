"""
Makhai Morgan
Oct 6, 2025
lab 8, unit test, bank account
"""

class Bankaccount:
    def __init__(self, user, pin , balance,):
        self.user = user
        self.pin = pin
        self.balance = balance

def deposit(self, amount):
    if amount <= 0:
        raise ValueError("Deposit amount must be positive!")
    self.balance += amount

def withdraw(self, amount):
    if amount > self.balance:
        raise ValueError("Insufficient funds for this withdrawal!")
    
    if amount <= 0:
        raise ValueError("Withdrawal amount must be positive!")
    
    self.balance -= amount

def get_balance(self):
    return self.balance
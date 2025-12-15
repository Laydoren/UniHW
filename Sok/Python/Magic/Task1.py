class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            raise ValueError("The deposit amount must be a positive number")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("The withdraw amount must be a positive number")

        if amount > self._balance:
            raise ValueError("Insufficient funds in account")

        self._balance -= amount

    def transfer(self, other_account, amount):
        if amount <= 0:
            raise ValueError("The transfer amount must be a positive number")

        if amount > self._balance:
            raise ValueError("Insufficient funds in account")

        self._balance -= amount
        other_account.deposit(amount)


print("Create account")
account1 = BankAccount(100)
account2 = BankAccount()

print(f"Account 1 bal: {account1.get_balance()}")
print(f"Account 2 bal: {account2.get_balance()}")

print("\nDeposit account 2")
account2.deposit(50)
print(f"Account 2 bal: {account2.get_balance()}")

print("\nWithdraw account 1")
try:
    account1.withdraw(30)
    print(f"Account 1 bal: {account1.get_balance()}")
except ValueError as e:
    print(f"Err whle withdraw: {e}")

print("\nTransfer")
try:
    account1.transfer(account2, 50)
    print(f"Account 1 bal: {account1.get_balance()}")
    print(f"Account 2 bal: {account2.get_balance()}")
except ValueError as e:
    print(f"Err while transfer: {e}")
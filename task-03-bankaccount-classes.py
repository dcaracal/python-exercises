class BankAccount:
    def __init__(self, account_number, initial_balance, interest_rate):
        self.account_number = account_number
        self.balance = initial_balance
        self.interest_rate = interest_rate

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount. Amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def calculate_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        print(f"Interest earned: ${interest:.2f}. New balance: ${self.balance:.2f}")

    def get_balance(self):
        return self.balance

# Example usage:
account = BankAccount("12345", 1000, 2.5)
account.deposit(500)
account.withdraw(200)
account.calculate_interest()
print("Final balance:", account.get_balance())
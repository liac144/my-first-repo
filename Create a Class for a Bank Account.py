class BankAccount:
    def __init__(self, account_number):
        self.account_number = account_number
        self.balance = 0  # Initialize balance to 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew: ${amount:.2f}. New balance: ${self.balance:.2f}")
            else:
                print("Insufficient funds for this withdrawal.")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"BankAccount(account_number={self.account_number}, balance=${self.balance:.2f})"

# Example usage
if __name__ == "__main__":
    # Create an instance of BankAccount
    account = BankAccount("123456789")
    
    # Deposit some money
    account.deposit(150.00)
    
    # Withdraw some money
    account.withdraw(50.00)
    
    # Display the account's balance
    print(f"Current balance: ${account.get_balance():.2f}")
    
    # Print the account details
    print(account)

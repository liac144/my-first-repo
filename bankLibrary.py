class BankAccount:
    def __init__(self, account_number):
        self.account_number = account_number
        self.balance = 0  # Initialize balance to 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited: ${amount:.2f}. New balance: ${self.balance:.2f}"
        else:
            return "Deposit amount must be positive."

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                return f"Withdrew: ${amount:.2f}. New balance: ${self.balance:.2f}"
            else:
                return "Insufficient funds for this withdrawal."
        else:
            return "Withdrawal amount must be positive."

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"BankAccount(account_number={self.account_number}, balance=${self.balance:.2f})"

class ChatBot:
    def __init__(self, account):
        self.account = account

    def respond(self, user_input):
        user_input = user_input.lower()
        if "balance" in user_input:
            return f"Your current balance is: ${self.account.get_balance():.2f}"
        elif "deposit" in user_input:
            amount = self.extract_amount(user_input)
            return self.account.deposit(amount)
        elif "withdraw" in user_input:
            amount = self.extract_amount(user_input)
            return self.account.withdraw(amount)
        else:
            return "I didn't understand that. You can ask about your balance, deposit funds, or withdraw funds."

    def extract_amount(self, user_input):
        # Simple extraction of the amount from user input
        words = user_input.split()
        for word in words:
            try:
                amount = float(word)
                return amount
            except ValueError:
                continue
        return 0  # Default to 0 if no valid amount is found

# Example usage
if __name__ == "__main__":
    account = BankAccount("123456789")
    chatbot = ChatBot(account)

    print("Welcome to the Bank Chatbot! You can ask about your balance, deposit, or withdraw funds.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Chatbot: Goodbye!")
            break
        response = chatbot.respond(user_input)
        print(f"Chatbot: {response}")

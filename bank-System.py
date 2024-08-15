class Account:
    def __init__(self, account_id, account_type, balance=0):
        self.account_id = account_id
        self.account_type = account_type  # E.g., 'Savings', 'Checking'
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount >= 50:
            self.balance += amount
            self.transactions.append(f"Deposited {amount}")
        else:
            print("Deposit amount must be at least 50 pounds.")

    def withdraw(self, amount):
        if 50 <= amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrew {amount}")
        else:
            print("Insufficient balance or invalid amount.")

    def transfer(self, amount, target_account):
        if 10 <= amount <= self.balance:
            self.withdraw(amount)
            target_account.deposit(amount)
            self.transactions.append(f"Transferred {amount} to account {target_account.account_id}")
            target_account.transactions.append(f"Received {amount} from account {self.account_id}")
        else:
            print("Transfer failed due to insufficient balance or invalid amount.")

    def check_balance(self):
        return self.balance

    def generate_statement(self):
        statement = f"Account Statement for Account ID {self.account_id}:\n"
        for transaction in self.transactions:
            statement += f"- {transaction}\n"
        statement += f"Current Balance: {self.balance}\n"
        return statement


class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def get_account(self, account_id):
        for account in self.accounts:
            if account.account_id == account_id:
                return account
        print("Account not found.")
        return None

    def list_accounts(self):
        return [account.account_id for account in self.accounts]


class Bank:
    def __init__(self, bank_name):
        self.bank_name = bank_name
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def get_customer(self, customer_id):
        for customer in self.customers:
            if customer.customer_id == customer_id:
                return customer
        print("Customer not found.")
        return None

    def list_customers(self):
        return [customer.name for customer in self.customers]


bank = Bank("My Bank")


customer1 = Customer(1, "John Doe")
customer2 = Customer(2, "Jane Smith")

bank.add_customer(customer1)
bank.add_customer(customer2)


account1 = Account(101, "Checking", 1500)
account2 = Account(102, "Savings", 1000)


customer1.add_account(account1)
customer1.add_account(account2)


account1.transfer(200, account2)


print(account1.check_balance())  
print(account2.check_balance())  
print(account1.generate_statement())  

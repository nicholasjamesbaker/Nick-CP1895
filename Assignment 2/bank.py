class BankAccount:
    def __init__(self, account_id: str, balance: float):
        self.__account_id = account_id
        self.__balance = balance
        self.__transaction_list = []

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount
        return True

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            return True
        else:
            print("Cannot withdraw more than your balance")
            return False

class Transaction:
    def __init__(self, from_account: BankAccount, to_account: BankAccount, amount: float):
        self.__to_account = to_account
        self.__from_account = from_account
        self.amount = amount
        if amount <= from_account.balance:
            to_account.deposit(amount)
            from_account.withdraw(amount)
        else:
            raise ValueError("Insufficent funds")


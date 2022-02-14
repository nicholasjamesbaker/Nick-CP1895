class BankAccount:
    def __init__(self, account_id: str, balance: float, transaction_list: list):
        self.__account_id = account_id
        self.__balance = balance
        self.__transaction_list = transaction_list

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

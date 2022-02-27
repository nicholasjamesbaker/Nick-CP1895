from bank import BankAccount


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



class BankException(Exception):
    def __init__(self, message):
        super().__init__(message)


class Bank(BankException):
    def __init__(self):
        self.__accounts = {}
        self._top_account = {}

    def new_account(self):
        self.__accounts[len(self.__accounts)+1] = 0
        self._top_account[len(self._top_account)+1] = 0

    def deposit(self, account, amount):
        if not account in self.__accounts:

            return False
        self.__accounts[account] = self.__accounts[account] + amount
        self._top_account[account] += 1
        return True

    def transfer(self, account1, account2, amount):
        if not account1 in self.__accounts or not account2 in self.__accounts:
            return False
        if amount > self.__accounts[account1]:
            return False
        self.withdraw(account1, amount)
        self.deposit(account2, amount)

    def withdraw(self, account, amount):
        if not account in self.__accounts:
            return False
        if amount > self.__accounts[account]:
            return False
        self.__accounts[account] -= amount
        self._top_account[account] += 1

    def get_account(self):
        return self.__accounts

bank_object = Bank()
bank_object.new_account()
print(bank_object.get_account())
bank_object.deposit(1,10)
print(bank_object.get_account())
bank_object.new_account()
print(bank_object.get_account())
bank_object.transfer(1,2,5)
print(bank_object.get_account())
ok = dict(sorted(bank_object._top_account.items(), key=lambda item: item[1], reverse=True))
ac, xd = list(ok.items())[0]
print("top activity account")
print(ac)
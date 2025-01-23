class Bank(object):

    def __init__(self, balance):
        """
        :type balance: List[int]
        """
        self.accounts = {}
        for accnt, amnt in enumerate(balance, start=1):
            self.accounts[accnt] = amnt
        

    def transfer(self, account1, account2, money):
        """
        :type account1: int
        :type account2: int
        :type money: int
        :rtype: bool
        """
        if not account1 in self.accounts:
            return False
        if not account2 in self.accounts:
            return False
        if money > self.accounts[account1]:
            return False
        self.withdraw(account1, money)
        self.deposit(account2, money)
        return True

    def deposit(self, account, money):
        """
        :type account: int
        :type money: int
        :rtype: bool
        """
        if not account in self.accounts:
            return False
        self.accounts[account] += money
        return True       

    def withdraw(self, account, money):
        """
        :type account: int
        :type money: int
        :rtype: bool
        """
        if not account in self.accounts:
            return False
        if money > self.accounts[account]:
            return False
        self.accounts[account] -= money
        return True 
        


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
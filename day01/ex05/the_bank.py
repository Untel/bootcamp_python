class Account(object):
    ID_COUNT = 1
    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
        print(self.__dict__)
        if hasattr(self, 'value'):
            self.value = 0
            Account.ID_COUNT += 1
    def transfer(self, amount):
        self.value += amount

    def __str__(self):
        txt = "Acc " + self.name + "\n"
        if hasattr(self, 'value'):
            txt += "Value: " + str(self.value) + "\n\n"
        return txt

class Bank(object):
    """The bank"""
    def __init__(self):
        self.account = []
    def add(self, account):
        self.account.append(account)
    def transfer(self, origin, dest, amount):
        """
            @origin: int(id) or str(name) of the first account
            @dest:    int(id) or str(name) of the destination account
            @amount: float(amount) amount to transfer
            @return         True if success, False if an error occured
        """
    def fix_account(self, account):
        """
            fix the corrupted account
            @account: int(id) or str(name) of the account
            @return         True if success, False if an error occured
        """


# Testcase
bank = Bank()
a = Account("A", value = 1000)
b = Account("B", value = 1000)
bank.add(a)
bank.add(b)
a.transfer(5000)
b.transfer(4000)
for acc in bank.account:
    print(acc.__dict__)
class Account(object):
    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
        if hasattr(self, 'value'):
            self.value = 0
        Account.ID_COUNT += 1

    def transfer(self, amount):
        self.value += amount


class Bank(object):
    """The bank"""
    def __init__(self):
        self.account = []

    def add(self, account):
        self.account.append(account)

    def transfer(self, origin, dest, amount):
        """
        Function to transfer money between accounts
        :param origin: int(id) or str(name) of first account
        :param dest: int(id) or str(name) of the destination account
        :param amount: float(amount) amount to transfer
        """
        pass

    def fix_account(self, account):
        pass

    def check_account(account):
        keys = account.keys()
        if len(keys) % 2 == 0:
            return False
        if 'name' not in keys or 'id' not in keys or 'value' not in keys:
            return False
        if 'zip' not in keys or 'addr' not in keys:
            return False
        for x in keys:
            if str(x).startswith('b'):
                return False
        return True

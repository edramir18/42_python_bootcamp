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
        origin = self.find_account(origin)
        dest = self.find_account(dest)
        if origin is None or dest is None:
            return False
        pass

    def find_account(self, value):
        key = None
        if isinstance(value, str):
            key = 'name'
        elif isinstance(value, int):
            key = 'id'
        if key is None:
            return None
        for x in self.account:
            if x[key] == value:
                return x
        return None

    def fix_account(self, account):
        pass

    @staticmethod
    def check_account(account):
        keys = account.keys()
        if len(keys) % 2 == 0:
            return False
        if any([x not in keys1 for x in ['name', 'id', 'value', 'zip', 'addr']]):
            return False
        if any([str(x).startswith('b') for x in keys]):
            return False
        return True

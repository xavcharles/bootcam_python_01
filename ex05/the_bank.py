class Account(object):
    
    ID_COUNT = 1
    
    def __init__(self, name, **kwargs):
        self.__dict__.update(kwargs)
        self.id = self.ID_COUNT
        Account.ID_COUNT += 1
        self.name = name
        if not hasattr(self, 'value'):
            self.value = 0
        if self.value < 0:
            raise AttributeError("Attribute value cannot be negative.")
        if not isinstance(self.name, str):
            raise AttributeError("Attribute name must be a str object.")
    
    def transfer(self, amount):
        self.value += amount

class Bank(object):
    """The bank"""
    def __init__(self):
        self.accounts = []

    def isCorrupted(self, name):
        for acc in self.accounts:
            if (acc.name == name):
                attributes = acc.__dict__
                attr_nb = len(attributes)
                if (attr_nb % 2 == 1):
                    return True
                cpt = 0
                for att in attributes.keys():
                    if (att[0] == 'b'):
                        return True
                    elif (len(att) >= 3 and att[:3] == "zip"):
                        cpt += 1
                    elif (len(att) >= 4 and att[:4] == "addr"):
                        cpt += 1
                    elif (att == "id"):
                        if not isinstance(acc.id, int):
                            return True
                        cpt += 1
                    elif (att == "name"):
                        cpt += 1
                    elif (att == "value"):
                        if not (isinstance(acc.value, int) or isinstance(acc.value, float)):
                            return True
                        cpt += 1
                if cpt < 5:
                    return True
                    


    def add(self, new_account):
        """ Add new_account in the Bank
        @new_account: Account() new account to append
        @return True if success, False if an error occured
        """
        # test if new_account is an Account() instance and if
        # it can be appended to the attribute accounts
        # ... Your code ...
        if not (isinstance(new_account, Account) and (new_account.name not in names for accs in self.accounts for names in accs.name)):
            return False
        self.accounts.append(new_account)
        return True


    def transfer(self, origin, dest, amount):
        """" Perform the fund transfer
        @origin: str(name) of the first account
        @dest: str(name) of the destination account
        @amount: float(amount) amount to transfer
        @return True if success, False if an error occured
        """
        found = 0
        for acc in self.accounts:
            if (isinstance(acc, Account) and isinstance(acc.name, str) and acc.name == origin):
                found += 1
                if (self.isCorrupted(origin) or amount > acc.value):
                    return False
            else:
                return False
            if (isinstance(acc, Account) and isinstance(acc.name, str) and acc.name == dest):
                found += 1
                if (self.isCorrupted(dest)):
                    return False
            else:
                return False
        if found != 2:
            return False
        for acc in self.accounts:
            if (acc.name == origin):
                acc.value -= amount
            elif (acc.name == dest):
                acc.value += amount
        return True


    def fix_account(self, name):
        """ fix account associated to name if corrupted
        @name: str(name) of the account
        @return True if success, False if an error occured
        """
        for acc in self.accounts:
            if (acc.name == name):
                attributes = acc.__dict__
                cpt = 0
                for att in attributes.keys():
                    if (att[0] == 'b'):
                        del acc.__dict__[att]
                    elif (len(att) >= 3 and att[:3] == "zip"):
                        cpt += 1
                    elif (len(att) >= 4 and att[:4] == "addr"):
                        cpt += 1
                    elif (att == "id"):
                        if not isinstance(acc.id, int):
                            acc.id = int(acc.id)
                        cpt += 1
                    elif (att == "name"):
                        cpt += 1
                    elif (att == "value"):
                        if not (isinstance(acc.value, int) or isinstance(acc.value, float)):
                            acc.value = float(acc.value)
                        cpt += 1
                if cpt < 5:
                    return True
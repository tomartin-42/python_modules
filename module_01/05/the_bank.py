import random
import string

# in the_bank.py
class Bank(object):
    """The bank"""
    def __init__(self):
        self.accounts = []

    def add(self, new_account):
        """ Add new_account in the Bank
        @new_account: Account() new account to append
        @return True if success, False if an error occured
        """
        if not isinstance(new_account, Account):
            return False
        if not self.search_account(new_account.name) == None:
            return False

    # test if new_account is an Account() instance and if
    # it can be appended to the attribute accounts
    # ... Your code ...

        self.accounts.append(new_account)
        return True

    def transfer(self, origin, dest, amount):
        if not isinstance(amount, int) and not isinstance(amount, float):
            return False
        c_origin = self.search_account(origin)
        c_dest = self.search_account(dest)
        if c_origin == None or c_dest == None:
            return False
        if c_origin == c_dest:
            return True
        if amount < 0:
            return False
        if (c_origin.value) - amount < 0 :
            return False
        else:
            c_origin.value -= amount
            c_dest.value += amount


        """" Perform the fund transfer
        @origin: str(name) of the first account
        @dest: str(name) of the destination account
        @amount: float(amount) amount to transfer
        @return True if success, False if an error occured
        """
    # ... Your code ...

    def fix_account(self, name):
        if not isinstance(name, str):
            return False
        aux_acc = self.search_account(name)
        if aux_acc == None:
            return False
        print(aux_acc.name)
        self.del_b_attr(aux_acc)                #del b attr
        self.zip_attr(aux_acc)                  #to zip and addr
        self.no_name(aux_acc)                   #to name
        self.no_id(aux_acc)
        self.no_value(aux_acc)
        if not len(aux_acc.__dict__)%2:         #even attr number
            self.new_random_attr(aux_acc)
            print(aux_acc.__dict__)
        """ fix account associated to name if corrupted
        @name: str(name) of the account
        @return True if success, False if an error occured
        """
    # ... Your code ...

    def search_account(self, name):
        for e in self.accounts:
            if name == e.name:
                return e
        return None

    def new_random_attr(self, aux_acc): # to even attr numbers
        chars = string.printable
        new_attr = 'X' + ''.join(random.choice(chars) for i in range(10))
        setattr(aux_acc, new_attr, 0)

    def del_b_attr(self, aux_acc): # del b attr
        for e in aux_acc.__dict__:
            if e[0] == 'b':
                delattr(aux_acc, e)

    def zip_attr(self, aux_acc):  # attr dont have zip or addr
        for e in aux_acc.__dict__:
            if e[0:2] == "zip" or e[0:3] == "addr":
                return None
        setattr(aux_acc, "zip", 0)

    def no_name(self, aux_acc):
        if "name" not in aux_acc.__dict__:
            setattr(aux_acc, "name", "0000")
        if not isinstance(aux_acc.name, str):
            delattr(aux_acc, "name")
            setattr(aux_acc, "name", "0000")

    def no_id(self, aux_acc):
        if "id" not in aux_acc.__dict__:
            setattr(aux_acc, "id", 0)
        if not isinstance(aux_acc.id, int):
            delattr(aux_acc, "id")
            setattr(aux_acc, "id", 0)

    def no_value(self, aux_acc):
        if "value" not in aux_acc.__dict__:
            setattr(aux_acc, "value", 0.0)
        if not isinstance(aux_acc.value, int) and not isinstance(aux_acc, float):
            delattr(aux_acc, "value")
            setattr(aux_acc, "value", 0.0)


# in the_bank.py
class Account(object):
    
    ID_COUNT = 1

    def __init__(self, name=None, **kwargs):
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
        elf.value += amount

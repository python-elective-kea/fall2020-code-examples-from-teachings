"""
2. Bank 
In the exercise from last monday with the bank, account and customer, change the code to use properties instead of the public variables.  
The bank class should futher be change into not taking any accounts as parameters at initialization. The accouts should be added afterwards, eithers as a single account one at a time, or as a collection of accounts (many at the sametime).      
Somewhere you should change the code so that a customer only can create one account.     
The Customer class should make sure that the customer is over 18 year of age.

"""

class Bank:    
    def __init__(self):
        self.__accounts = []  # When bank is initialized it has  the abillity to hold many accounts
    
    @property
    def accounts(self):
        return self.__accounts

    @accounts.setter
    def accounts(self, acc):
        if type(acc) in [list, tuple, set]:
            for i in acc:
                self.__has_account(i)
                self.__accounts.append(i)
        else:
            self.__has_account(acc)
            self.__accounts.append(acc)


    def __has_account(self, acc):
        for i in self.accounts:
            if acc.cust.name == i.cust.name:
                raise ValueError('Customer aleready has an account!')
        return False

class Account:
    def __init__(self, no, cust):
        self.no = no
        self.cust = cust

    # no
    @property
    def no(self):
        return self.__no

    @no.setter
    def no(self, no):
        self.__no = no

    # cust
    @property
    def cust(self):
        return self.__cust

    @cust.setter
    def cust(self, cust):
        self.__cust = cust

    def __repr__(self):
        return str(self.__dict__)


class Customer:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age < 18:
            raise ValueError('You must be 18 or above to create an account')
        self.__age = age

    def __repr__(self):
        return str(self.__dict__)

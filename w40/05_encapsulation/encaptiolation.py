"""
Encaptiolation &  Propeties exercises
All following exercises should be done by using Properties when needed. The focus should be on encapsulation. 

1. Car object
Create a Car class. 
When instanciated the object should be able to take 4 attributes (Make, Model, bhp, mph).
They all 4 should be properties.

"""

"""
2. Bank 
In the exercise from last monday with the bank, account and customer, change the code to use properties instead of the public variables.  
The bank class should futher be change into not taking any accounts as parameters at initialization. The accouts should be added afterwards, eithers as a single account one at a time, or as a collection of accounts (many at the sametime).      
Somewhere you should change the code so that a customer only can create one account.     
The Customer class should make sure that the customer is over 18 year of age.

"""

class Bank:    
    def __init__(self):
        self.__accounts = []  # initialize the private variable as a list
    
    @property
    def accounts(self):
        return self.__accounts

    @accounts.setter
    def accounts(self, acc):
        self.__accounts.append(acc)


class Account:
    def __init__(self, no, cust):
        self.__no = no
        self.__cust = cust
    def __repr__(self):
        return str(self.__dict__)


class Customer:
    def __init__(self, name):
        self.__name = name

    def __repr__(self):
        return str(self.__dict__)
"""
3. Machine -> printer
Create a Machine class that takes care of powering on and off a the machine.   
Create a printer class that is a subclass of the Machine super class.   
The printer should be able to print to console.  
The printer should have a papertray, which should be in its own class. The papertray class should keep track of the paper, it should have the abillity to use paper and and load new paper in the tray if empty.  

"""


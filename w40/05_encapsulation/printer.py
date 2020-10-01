# printer.py (solution)

"""
    3. Machine -> printer
    Create a Machine class that takes care of powering on and off a the machine.   
    Create a printer class that is a subclass of the Machine super class.   
    The printer should be able to print to console.  
    The printer should have a papertray, which should be in its own class. The papertray class should keep track of the paper, it should have the abillity to use paper and and load new paper in the tray if empty.  
"""

class Machine:
    """ takes care of turning on and off  """

    def __init__(self):
        self.__is_on = False

    @property
    def is_on(self):
        return self.__is_on

    def power(self):
        self.__is_on = not self.__is_on

class Printer(Machine):
    def __init__(self):
        # 1.
        super().__init__()

        # 2.
        # Machine.__init__(self)
        
        self.__pt = Papertray()

    def print(self, text):
        if self.__pt.paper == 0:
            print('Papertray is empty')
        else:
            if self.is_on:
                print(text)
                self.__pt.paper = self.__pt.paper - 1
            else:
                print('Printer is off')

    @property
    def load(self):
        return self.__pt.paper

    load.setter
    def load(self, no):
        self.__pt.paper = no

class Papertray:
    def __init__(self):
        self.paper = 2

    @property
    def paper(self):
        return self.__paper

    @paper.setter
    def paper(self, paper):
        self.__paper = paper










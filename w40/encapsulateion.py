class P:
    def __init__(self, name, alias):
        #self.name = name # porperty
        #self.alias = alias # public variable
        pass

    @property  # getter
    def name(self):
        return self.__name

    @name.setter
    def name(self, *args):
        if args[0][0] == 'C':
            self.__name = args[0]
    
"""
    @property
    def alias(self):
        return self.__alias

    @alias.setter
    def alias(self, x):
        self.__alias = x
"""

# bad vay JAVA Style

"""
    def get_alias(self):
        return self.__alias

    def set_alias(self, x):
        self.__alias = x

    def get_name(self):
        return self.name


    def set_name(self, x):
        self.name = x

"""

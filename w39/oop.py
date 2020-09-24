from inst import *

class Person:

    # type = 'Mammel'
    
    def __init__(self, *args):
        if len(args) == 1:
            self.name = args[0]
        if len(args) == 2:
            self.name = args[0]
            self.last = args[1]
        else:
            raise Exception()


    def full_name(self):
        return self.name + ' ' + self.last + ' ' + self.funny 

    def funny_Age(self):
        self.funny = 'Ha ha ha'






#class Instructor:
#    def __init__(self, name):
#        self.name = name

class Gender:
    def __init__(self, s):
        self.sex = s

class Student(Instructor, Gender):
    def __init__(self, *args):
        # super().__init__(args[0])
        Instructor.__init__(self, args[0])
        Gender.__init__(self, args[1])
        self.salary = args[2]
















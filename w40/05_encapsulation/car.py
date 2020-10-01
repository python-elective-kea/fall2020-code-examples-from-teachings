# car.py (solution)

1. Car object
Create a Car class. 
When instanciated the object should be able to take 4 attributes (Make, Model, bhp, mph).
They all 4 should be properties.

class Car:
    def __init__(self, *args):
        self.make = args[0]
        self.model = args[1]
        self.bhp = args[2]
        self.mph = args[3]

    // make
    @property 
    def make(self):
        return self.__make
    
    @make.setter
    def make(self, make):
        self.__make = make



    // model
    @property 
    def model(self):
        return self.__model
    
    @model.setter
    def make(self, model):
        self.__model = model


    
    // bhp
    @property 
    def bhp(self):
        return self.__bhp
    
    @bhp.setter
    def make(self, bhp):
        self.__bhp = bhp



    // mph
    @property 
    def mph(self):
        return self.__mph
    
    @mph.setter
    def mph(self, mph):
        self.__mph = mph


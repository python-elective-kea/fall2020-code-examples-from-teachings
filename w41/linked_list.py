class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.__dict__)

class LinkedList:
    def __init__(self):
        self.head = None

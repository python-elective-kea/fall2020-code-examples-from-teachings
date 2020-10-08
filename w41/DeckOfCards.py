
class Deck:

    def __init__(self):
        self.cards = ['A', 'K', 4, 7]

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, x):
        return self.cards[x]


    def __add__(self, other):
        d = Deck()
        d.cards = self.cards + other.cards
        return d

    def __repr__(self):
        return str(self.__dict__)   

    def __str__(self):
        return f'Cards: {self.cards}'
        
    def __setitem__(self, key, value):
        self.cards[key] = value

    def __delitem__(self, x):
        del(self.cards[x])

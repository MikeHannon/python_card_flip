import random
print ('cards class')
class Cards(object):
    """docstring for cards"""
    def __init__(self):
        super(Cards, self).__init__()
        suits = ('hearts','diamonds', 'clubs', 'spades')
        values = ('ace','king','queen','jack','10','9','8','7','6','5','4','3','2')
        self.deck = []
        for suit in suits:
            for value in values:
                self.deck.append({'values':value, 'suits':suit, 'image':'images/Playing_Cards/PNGs/'+value+'_of_'+suit+'.png', 'alternate':'images/Playing_Cards/PNGs/cardback.png'})
    def shuffle(self):
        temp_deck = []
        #go through current deck, find random card, append temp_deck, remove from current deck, at the end set to current deck to temp_deck
        while len(self.deck) > 0:
            temp_val = random.randrange(0,len(self.deck))
            # this method allows to pop and append in oneline
            temp_deck.append(self.deck.pop(temp_val))
        self.deck = temp_deck
        return self

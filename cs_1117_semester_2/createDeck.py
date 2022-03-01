from random import shuffle

def createDeck():
    """ A standard deck of cards contains 52 cards. 
    This  function  uses  nested  loops  to  create  a  complete 
    deck (list) of cards (52 in total) by storing the 2 character abbreviations in a new list."""
    
    suits = ["s", "h", "d", "c"]
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]

    newDeck = []

    for suit in suits:
        for value in values:
            newDeck.append(value + suit)
        
    return (newDeck)

deck = createDeck()
print(deck)
print (len(deck))
shuffle(deck)
print(deck)
print (len(deck))
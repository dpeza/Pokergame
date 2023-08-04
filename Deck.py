from Card import Card
HAND_DICT = {5:"flush", 4:"straight", 3:"two-pairs", 2:"one-pair", 1:"highest-card"}
CARD_DICT = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7":7,"8":8,"9":9,"10":10,"J":11,"Q":12,"K":13,"A":14}
class Deck:
    cards = []
    VALUES = ["2", "3", "4", "5", "6", "7","8","9","10","J","Q","K","A"]
    SUITS = ["Spades","Hearts","Clubs","Diamonds"]
    def __init__(self):
        self.makeDeck()

    def makeDeck(self):
        for suit in self.SUITS:
            for value in self.VALUES: 
                self.cards.append(Card(suit, value))
    def __str__(self) -> str:
        output = []
        for i in self.cards: output.append(str(i))
        return str(output)


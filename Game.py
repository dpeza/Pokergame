import random
from Hand import Hand
from Deck import Deck
HAND_DICT = {5:"flush", 4:"straight", 3:"two-pairs", 2:"one-pair", 1:"highest-card"}
CARD_DICT = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7":7,"8":8,"9":9,"10":10,"J":11,"Q":12,"K":13,"A":14}
class Game:
    hands = []
    winner = 0
    def __init__(self, players, deck) -> None:
        self.players = players
        self.deck = deck
        self.deal()
        self.find_better_hand()
    def deal(self):
        for i in range(self.players):
            cards = []
            for i in range(5):
                card = random.choice(self.deck.cards)
                self.deck.cards.remove(card)
                cards.append(card)
            self.hands.append(Hand(cards))
    def find_better_hand(self):
        if self.hands[0].hand_Value > self.hands[1].hand_Value:
            self.winner=0
            return 
        elif self.hands[0].hand_Value < self.hands[1].hand_Value:
            self.winner=1
            return 
        else: 
            self.tie_break()

    def tie_break(self):
        player1 = self.hands[0]
        player2 = self.hands[1]
        if self.hands[0].hand_Value == 1: #tie break for high card
            for i in range(4):
                if player1.values[4-i] > player2.values[4-i]:
                    self.winner = 0
                    return
                elif player1.values[4-i] < player2.values[4-i]:
                    self.winner = 1
                    return

        elif self.hands[0].hand_Value == 2: # tie break for pair
            if player1.get_pair_value() > player2.get_pair_value():
                self.winner = 0
                return
            elif player1.get_pair_value() < player2.get_pair_value():
                self.winner = 1
                return
            else:
                return 
        elif self.hands[0].hand_Value == 3:# tie break for two pair
            if player1.get_two_pair_value()[1] > player1.get_two_pair_value()[1]:
                self.winner = 0
                return
            elif player1.get_two_pair_value()[1] < player1.get_two_pair_value()[1]:
                self.winner = 1
                return
            else:
                if player1.get_two_pair_value()[0] > player1.get_two_pair_value()[0]:
                    self.winner = 0
                    return
                elif player1.get_two_pair_value()[0] < player1.get_two_pair_value()[0]:
                    self.winner = 1
                    return

        elif self.hands[0].hand_Value == 4: # tie break for straight
            if player1.values[4] > player2.values[4]:
                self.winner = 0
                return
            elif player1.values[4] < player2.values[4]:
                self.winner = 1
                return

        elif self.hands[0].hand_Value == 5:
            if player1.values[4] > player2.values[4]:
                self.winner = 0
                return
            elif player1.values[4] < player2.values[4]:
                self.winner = 1
                return
    def __str__(self) -> str:
        if self.winner == 0:
            return f"Player 1 has hand: {str(self.hands[0])} \n Player 2 has hand: {str(self.hands[1])} \n Player {self.winner+1} wins with {HAND_DICT[self.hands[0].hand_Value]}"
        elif self.winner == 1:
            return f"Player 1 has hand: {str(self.hands[0])} \n Player 2 has hand: {str(self.hands[1])} \n Player {self.winner+1} wins with {HAND_DICT[self.hands[1].hand_Value]}"
        else:
            return "error"

print(Game(2, Deck()))

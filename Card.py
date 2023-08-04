import itertools
import random
import unittest

HAND_DICT = {5:"flush", 4:"straight", 3:"two-pairs", 2:"one-pair", 1:"highest-card"}
CARD_DICT = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7":7,"8":8,"9":9,"10":10,"J":11,"Q":12,"K":13,"A":14}
class Card:
    def __init__(self, suit, value) -> None:
        self.suit = suit
        self.value = value

    def __str__(self) -> str:
        return f"{self.value} of {self.suit}"

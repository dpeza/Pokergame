
import unittest
from Hand import Hand
from Card import Card

class TestCalculations(unittest.TestCase):
    HANDS = [
        [Card("Spades", "2"),Card("Diamonds", "7"),Card("Clubs", "8"),Card("Diamonds", "4"),Card("Spades", "A")], #high card
        [Card("Spades", "2"),Card("Diamonds", "7"),Card("Clubs", "4"),Card("Diamonds", "4"),Card("Spades", "A")], #one pair
        [Card("Spades", "7"),Card("Diamonds", "7"),Card("Clubs", "4"),Card("Diamonds", "4"),Card("Spades", "A")], #two pair
        [Card("Spades", "2"),Card("Diamonds", "3"),Card("Clubs", "4"),Card("Diamonds", "5"),Card("Spades", "6")], #straight
        [Card("Spades", "2"),Card("Spades", "7"),Card("Spades", "4"),Card("Spades", "4"),Card("Spades", "A")], #flush
    ]
    def test_pair(self):
        hand = Hand(self.HANDS[1])
        self.assertEqual(hand.evaluate_hand(), 2, 'Pair Failed')
        hand = Hand(self.HANDS[0])
        self.assertEqual(hand.evaluate_hand(), 1, 'Pair Failed')
    def test_flush(self):
        hand = Hand(self.HANDS[4])
        self.assertEqual(hand.evaluate_hand(), 5, 'Flush Failed')
    def test_straight(self):
        hand = Hand(self.HANDS[3])
        self.assertEqual(hand.evaluate_hand(), 4, 'Straight Failed')
    def test_two_pair(self):
        hand = Hand(self.HANDS[2])
        self.assertEqual(hand.evaluate_hand(), 3, 'Straight Failed')

if __name__ == '__main__':
    unittest.main()
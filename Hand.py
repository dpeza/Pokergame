HAND_DICT = {5:"flush", 4:"straight", 3:"two-pairs", 2:"one-pair", 1:"highest-card"}
CARD_DICT = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7":7,"8":8,"9":9,"10":10,"J":11,"Q":12,"K":13,"A":14}
class Hand:    
    cards = []
    values = []
    hand_Value = 1
    def __init__(self, cards) -> None:
        self.cards = cards
        self.values = sorted(map(lambda card: CARD_DICT[card.value], self.cards))
        self.evaluate_hand()
        
    def has_pair(self):
        temp_set = set(self.values)
       
        if len(temp_set) == 4:
            return True
    def has_flush(self):
        suits = map(lambda card: card.suit, self.cards)
        temp_set = set(suits)
        if len(temp_set) == 1:
            return True
    def has_striaght(self):
        if self.values == list(range(self.values[0],self.values[4]+1)):
            
            return True
    def has_two_pair(self):
        dup_list = []
        check_list = []
        for i in self.values:
            if i not in check_list:
                check_list.append(i)
            else:
                dup_list.append(i)
        if len(dup_list) == 2:
            return True
    def get_pair_value(self):
        dup_list = []
        check_list = []
        for i in self.values:
            if i not in check_list:
                check_list.append(i)
            else:
                dup_list.append(i)
        if len(dup_list) == 1:
            return dup_list[0]
    def get_two_pair_value(self):
        dup_list = []
        check_list = []
        for i in self.values:
            if i not in check_list:
                check_list.append(i)
            else:
                dup_list.append(i)
        if len(dup_list) == 2:
            return sorted(dup_list)
    def get_high_card(self):
        return self.values[4]
    def evaluate_hand(self):
        if self.has_flush():
            self.hand_Value = 5
            return 5
        elif self.has_striaght(): 
            self.hand_Value = 4
            return 4
        elif self.has_two_pair(): 
            self.hand_Value = 3
            return 3
        elif self.has_pair():
            self.hand_Value = 2
            return 2
        else: 
            self.hand_Value = 1
            return 1
    def __str__(self) -> str:
        output = []
        for i in self.cards: output.append(str(i))
        return str(output)
    

from deck import Deck


class Poker(object):
    def __init__(self, num_hands):
        self.deck = Deck()
        self.deck.shuffle_deck()
        self.hands = []
        self.scoring = []
        self.burn = []
        self.current_table = []
        self.seven_card_hands = []

        for i in range(num_hands):
            hand = [self.deck.deal()]
            self.hands.append(hand)

        for j in range(num_hands):
            self.hands[j].append(self.deck.deal())

        # after all cards are dealt, burn 1 before the flop
        self.burn.append(self.deck.deal())

    def flop(self):
        for i in range(3):
            self.current_table.append(self.deck.deal())
        table = ""
        for card in self.current_table:
            table = table + str(card) + " "
        print(f"\nTable after Flop: {table}")

        # after flop, burn 1 before the turn
        self.burn.append(self.deck.deal())

    def turn(self):
        self.current_table.append(self.deck.deal())
        table = ""
        for card in self.current_table:
            table = table + str(card) + " "
        print(f"\nTable after Turn: {table}")

        # after turn, burn 1 before the river
        self.burn.append(self.deck.deal())

    def river(self):
        self.current_table.append(self.deck.deal())
        table = ""
        for card in self.current_table:
            table = table + str(card) + " "
        print(f"\nTable after River: {table}")

    def play(self):
        for i in range(len(self.hands)):
            sorted_hand = sorted(self.hands[i], reverse=True)
            hand = ""
            for card in sorted_hand:
                hand = hand + str(card) + " "
            print(f"Hand {str(i + 1)}: {hand}")

        self.flop()
        self.turn()
        self.river()

        for x in range(len(self.hands)):
            self.seven_card_hands.append(self.hands[x] + self.current_table)

        # TODO  : Implement a winning mechanism to determine the best 5 card hand
        # self.win()



# flop -> turn -> river
if __name__ == "__main__":
    poker = Poker(2)
    poker.play()




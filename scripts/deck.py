from card import Card as C
import random


class Deck(object):
    def __init__(self):
        self.deck = []
        for suit in C.SUIT:
            for rank in C.RANK:
                card = C(rank, suit)
                self.deck.append(card)

    def __len__(self):
        return len(self.deck)

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop(0) if len(self) > 0 else None

    def test_sorted_deck(self):
        for c in self.deck:
            print(c)

    def test_shuffled_deck(self):
        self.shuffle_deck()
        for c in self.deck:
            print(c)


if __name__ == "__main__":
    # To test that each card was correctly added to the deck
    deck = Deck()
    # deck.test_sorted_deck()
    # deck.test_shuffled_deck()


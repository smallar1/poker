class Card(object):
    RANK = (2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A') # Card Values
    SUIT = ('♠', '♣', '♦', '♥') # Card Suits

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f'{self.rank}{self.suit}'

    def __eq__(self, other):
        return self.rank == other.rank

    def __lt__(self, other):
        return self.rank < other.rank

    def __le__(self, other):
        return self.rank <= other.rank

    def __gt__(self, other):
        return self.rank > other.rank

    def __ge__(self, other):
        return self.rank >= other.rank

    def __ne__(self, other):
        return self.rank != other.rank

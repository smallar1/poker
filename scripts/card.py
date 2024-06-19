class Card(object):
    RANK = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14) # Card Values
    SUIT = ('♠', '♣', '♦', '♥') # Card Suits

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        if self.rank == 11:
            self.rank = 'J'
        elif self.rank == 12:
            self.rank = 'Q'
        elif self.rank == 13:
            self.rank = 'K'
        elif self.rank == 14:
            self.rank = 'A'
        return f'{self.rank}{self.suit}'

    def __eq__(self, other):
        return self.rank == other.rank

    def __lt__(self, other):
        if isinstance(self.rank, str) and isinstance(other.rank, int):
            return False
        elif isinstance(self.rank, int) and isinstance(other.rank, str):
            return True
        else:
            return self.rank < other.rank

    def __le__(self, other):
        return self.rank <= other.rank

    def __gt__(self, other):
        return self.rank > other.rank

    def __ge__(self, other):
        return self.rank >= other.rank

    def __ne__(self, other):
        return self.rank != other.rank

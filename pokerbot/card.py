class Card:
    """
    A class representing a poker card.

    Attributes
    ----------
        suit : int
            represents the suit of the card,
            with 0 = Club, 1 = Diamond, 2 = Heart, 3 = Spade
        rank : int
            represents the value of the card, with 2-10 representing 2-10,
            11 representing J, 12 representing Q, 13 representing Q,
            and 14 (note!) representing A

    Inspired from:
    https://github.com/ishikota/PyPokerEngine/blob/master/pypokerengine/engine/card.py

    """
    CLUB = 0
    DIAMOND = 1
    HEART = 2
    SPADE = 3

    SUIT_MAP = {0: 'C', 1: 'D', 2: 'H', 3: 'S'}
    RANK_MAP = {2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7',
                8: '8', 9: '9', 10: '10', 11: 'J', 12: 'Q', 13: 'K', 14: 'A'}

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = 14 if rank == 1 else rank

    def __eq__(self, card):
        return (self.suit == card.suit) and (self.rank == card.suit)

    def __str__(self):
        return self.SUIT_MAP[self.suit] + self.RANK_MAP[self.rank]

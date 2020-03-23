class Player:
    """
    A class representing a Poker player (private state) of a WSOP game.

    Attributes
    ----------
        name : str
            the name of the player
        card1 : Card
            the first card held by current player
        card2 : Card
            the second card held by the current player
        chips : int
            the number of chips the current player has remaining
    """
    def __init__(self, card1, card2, chips):
        self.card1 = card1
        self.card2 = card2
        self.chips = chips

    def __str__(self):
        return ("cards {" + str(self.card1) + ", "
                + str(self.card2) + "} chips: " + str(self.chips))

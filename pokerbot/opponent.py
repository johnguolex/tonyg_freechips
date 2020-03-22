class Opponent:
    """
    Class representing an opponent in WSOP online poker.

    Attributes
    ----------
    stack : int
        represents the amount of chips the opponent has left
    """

    def __init__(self, chips):
        self.chips = chips

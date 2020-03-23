class Opponent:
    """
    Class representing an opponent in WSOP online poker.
    Attributes
    ----------
    id : str
        an id representing the opponent
    chips : int
        represents the amount of chips the opponent has left
    """

    def __init__(self, id, chips):
        self.id = id
        self.chips = chips

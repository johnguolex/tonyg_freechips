class GameState:
    """
    A class representing a gamestate in Texas Hold'Em.

    Attributes
    ----------
        player : Player
            you (the player) of the WSOP game
        opponents : list Opponen
            a list of Opponents at the Poker Table
        round : int
            an int representing which stage of the hand we are at
        sharedcards : list Card
            a list of cards shared by all opponents, in the middle of the table

    """

    PREFLOP = 0
    FLOP = 3
    TURN = 4
    RIVER = 5

    ROUND_MAP = {0: 'Preflop', 3: 'Flop', 4: 'Turn', 5: 'River'}

    def __init__(self, player, opponents, round=PREFLOP, sharedcards=[]):
        self.player = player
        self.opponents = opponents
        self.round = round
        self.sharedcards = sharedcards

    def __str__(self):
        return ("player : " + str(self.player) + "currently in round : " +
                str(self.ROUND_MAP[self.round]) + " shared cards: " +
                str(self.sharedcards))

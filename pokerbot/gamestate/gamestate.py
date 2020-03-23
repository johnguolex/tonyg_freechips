class GameState:
    """
    A class representing a gamestate in Texas Hold'Em.

    Attributes
    ----------
        player : Player
            you (the player / private state) of the WSOP game
        table : Table
            the table (public state) of the WSOP game
    """

    def __init__(self, player, table):
        self.player = player
        self.table = table

    def __str__(self):
        return ("player : " + str(self.player) + " " + str(self.table))

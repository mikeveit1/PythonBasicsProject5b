class Taxicab:

    """Has three private data members: one that holds the current x-coordinate, one that holds the current y-coordinate,
        and one that holds the current odometer reading (the actual odometer distance driven by the Taxicab,
        not the Euclidean distance from its starting point). Has two methods that move the Taxicab object: one to move
        left/right(x), one to move up/down(y)"""

    def __init__(self, xCoord, yCoord):
        """Initializes the Taxicab object with an x-coordinate parameter, a y-coordinate parameter,
            and the odometer with 0"""
        self._xCoord = xCoord
        self._yCoord = yCoord
        self._odometer = 0

    def get_x_coord(self):
        """Returns the current x coordinate"""
        return self._xCoord

    def get_y_coord(self):
        """Returns the current y coordinate"""
        return self._yCoord

    def get_odometer(self):
        """Returns the current odometer reading"""
        return self._odometer

    def move_x(self, unitsToMove):
        """Takes in a parameter of units to move the Taxicab object left or right"""
        self._xCoord += unitsToMove
        self._odometer += abs(unitsToMove)

    def move_y(self, unitsToMove):
        """Takes in a parameter of units to move the Taxicab object up or down"""
        self._yCoord += unitsToMove
        self._odometer += abs(unitsToMove)

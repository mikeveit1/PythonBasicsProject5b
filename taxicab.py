class Taxicab:

    """Has three private data members: one that holds the current x-coordinate, one that holds the current y-coordinate,
        and one that holds the current odometer reading (the actual odometer distance driven by the Taxicab,
        not the Euclidean distance from its starting point). Has two methods that move the Taxicab object: one to move
        left/right(x), one to move up/down(y)"""

    def __init__(self, x_coord, y_coord):
        """Initializes the Taxicab object with an x-coordinate parameter, a y-coordinate parameter,
            and the odometer with 0"""
        self._x_coord = x_coord
        self._y_coord = y_coord
        self._odometer = 0

    def get_x_coord(self):
        """Returns the current x coordinate"""
        return self._x_coord

    def get_y_coord(self):
        """Returns the current y coordinate"""
        return self._y_coord

    def get_odometer(self):
        """Returns the current odometer reading"""
        return self._odometer

    def move_x(self, units_to_move):
        """Takes in a parameter of units to move the Taxicab object left or right"""
        self._x_Coord += units_to_move
        self._odometer += abs(units_to_move)

    def move_y(self, units_to_move):
        """Takes in a parameter of units to move the Taxicab object up or down"""
        self._y_coord += units_to_move
        self._odometer += abs(units_to_move)

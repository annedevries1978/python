# Globals for the bearings
# Change the values as you see fit
EAST = 'EAST'
NORTH = 'NORTH'
WEST = 'WEST'
SOUTH = 'SOUTH'

"""Robots are placed on a hypothetical infinite grid, facing a particular
direction (north, east, south, or west) at a set of {x,y} coordinates,
e.g., {3,8}, with coordinates increasing to the north and east.

The robot then receives a number of instructions, at which point the
testing facility verifies the robot's new position, and in which
direction it is pointing.
"""

class Robot(object):
    def __init__(self, bearing=NORTH, x=0, y=0):
        self.bearing = bearing
        self.x = x
        self.y = y


    def turn_left(self):
        self.bearing -= 1
        return self.bearing


    def turn_right(self):
        self.bearing += 1
        return self.bearing

    def advance(self):
        if self.bearing == EAST:
            self.x += 1
        elif self.bearing == NORTH:
            self.y += 1
        elif self.bearing == SOUTH:
            self.y -= 1
        else:
            self.bearing == WEST
            self.x -= 1

    def simulate(self, letters):
        pass

    @property
    def coordinates(self):
        return self.x, self.y


# robot = Robot(SOUTH, -1, 1)


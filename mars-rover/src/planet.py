import rover

class Planet:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def createRover(self, x, y, orientation):
        return rover.Rover(x, y, orientation, self)

    def wrap_x(self, x):
        return x % self.width

    def wrap_y(self, y):
        return y % self.height

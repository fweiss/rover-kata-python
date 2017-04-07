import rover

class Planet:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.obstacles = set()

    def createRover(self, x, y, orientation):
        return rover.Rover(x, y, orientation, self)

    def wrap_x(self, x):
        return x % self.width

    def wrap_y(self, y):
        return y % self.height

    def createPositionKey(self, x, y):
        return "{:d}:{:d}".format(x, y)

    def setObstacle(self, x, y):
        key = self.createPositionKey(x, y)
        self.obstacles.add(key)

    def checkObstacle(self, x, y):
        key = self.createPositionKey(x, y)
        return key in self.obstacles

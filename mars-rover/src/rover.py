class Rover:

    global commands
    global deltas

    def __init__(self, x, y, orientation, planet):
        self.x = x
        self.y = y
        self.orientation = orientation
        self.planet = planet

    def move(self, commands):
        for command in commands:
            self.moveBy(command)

    # use command pattern and lookup to avoid switch statements :)
    def moveBy(self, commandKey):
        command = commands[commandKey]
        delta = deltas[self.orientation]
        command(self, delta)

    def move_forward(self, delta):
        self.x = self.planet.wrap_x(self.x + delta[0])
        self.y = self.planet.wrap_y(self.y + delta[1])

    def move_backward(self, delta):
        self.x = self.planet.wrap_x(self.x - delta[0])
        self.y = self.planet.wrap_y(self.y - delta[1])

    def move_right(self, delta):
        self.orientation = delta[3]

    def move_left(self, delta):
        self.orientation = delta[2]

    # commands to dispatch for each move key
    commands = {
        'f': move_forward,
        'b': move_backward,
        'r': move_right,
        'l': move_left
    }

    # x,y deltas to move forward for each orientation
    # compoents are dx, dy, leftOrientation, rightOrientation
    deltas = {
        'N': [ +0, +1, 'W', 'E' ],
        'S': [ +0, -1, 'E', 'W' ],
        'E': [ +1, +0, 'N', 'S' ],
        'W': [ -1, +0, 'S', 'N' ]
    }

class Rover:

    global commands
    global deltas

    def __init__(self, x, y, orientation):
        self.x = x
        self.y = y
        self.orientation = orientation

    def move(self, commands):
        self.moveBy(commands[0])

    # use command pattern and lookup to avoid switch statements :)
    def moveBy(self, commandKey):
        command = commands[commandKey]
        delta = deltas[self.orientation]
        command(self, delta)

    def move_forward(self, delta):
        self.x += delta[0]
        self.y += delta[1]

    def move_backward(self, delta):
        self.x -= delta[0]
        self.y -= delta[1]

    # commands to dispatch for each move key
    commands = {
        'f': move_forward,
        'b': move_backward
    }

    # x,y deltas to move forward for each orientation
    deltas = {
        'N': [ +0, +1 ],
        'S': [ +0, -1 ],
        'E': [ +1, +0 ],
        'W': [ -1, +0 ]
    }

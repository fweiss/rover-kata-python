class Rover:

    global commands

    def __init__(self, x, y, orientation):
        self.x = x
        self.y = y
        self.orientation = orientation

    def move(self, commands):
        self.moveBy(commands[0])

    def moveBy(self, commandKey):
        command = commands[commandKey]
        command(self)

    def move_forward(self):
        self.y += 1

    def move_backward(self):
        self.y -= 1

    commands = {
        'f': move_forward,
        'b': move_backward
    }

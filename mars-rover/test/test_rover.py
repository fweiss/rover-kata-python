from nose.tools import *
import rover

class TestRover:

    def setup(self):
        global r
        r = rover.Rover(10, 21, 'N')

    def test_initial_x(self):
        assert_equal(10, r.x)

    def test_initial_y(self):
        assert_equal(21, r.y)

    def test_initial_orientation(self):
        assert_equal('N', r.orientation)

class TestMovesOrientationNorth:

    def setup(self):
        global r
        r = rover.Rover(10, 21, 'N')

    def test_move_f(self):
        r.move(list("f"))
        assert_equal(22, r.y)
        assert_equal(10, r.x)

    def test_move_b(self):
        r.move(list("b"))
        assert_equal(10, r.x)
        assert_equal(20, r.y)

class TestMovesOrientationSouth:

    def setup(self):
        # tried using self.r, but it gets too wordy using self.r everywhere
        global r
        r = rover.Rover(10, 21, 'S')

    def test_move_forward(self):
        r.move(list("f"))
        assert_equal(10, r.x)
        assert_equal(20, r.y)

    def test_move_backward(self):
        r.move(list("b"))
        assert_equal(10, r.x)
        assert_equal(22, r.y)

# would love use use test generators!
class TestMovesOrientationEast:

    def setup(self):
        global r
        r = rover.Rover(10, 21, 'E')

    def test_move_forward(self):
        r.move(list('f'))
        assert_equal(11, r.x)
        assert_equal(21, r.y)

    def test_move_backward(self):
        r.move(list("b"))
        assert_equal(9, r.x)
        assert_equal(21, r.y)

class TestMovesOrientationWest:

    def setup(self):
        global r
        r = rover.Rover(10, 21, 'W')

    def test_move_forward(self):
        r.move(list("f"))
        assert_equals(9, r.x)
        assert_equals(21, r.y)

    def test_move_backward(self):
        r.move(list("b"))
        assert_equal(11, r.x)
        assert_equal(21, r.y)

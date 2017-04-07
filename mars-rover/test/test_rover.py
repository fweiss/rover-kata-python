from nose.tools import *
import rover
import planet

def createRover(x, y, orientation):
    thePlanet = planet.Planet(100, 100)
    return thePlanet.createRover(x, y, orientation)

class TestRover:

    def setup(self):
        global r
        r = createRover(10, 21, 'N')

    def test_initial_x(self):
        assert_equal(10, r.x)

    def test_initial_y(self):
        assert_equal(21, r.y)

    def test_initial_orientation(self):
        assert_equal('N', r.orientation)

class TestMovesOrientationNorth:

    def setup(self):
        global r
        r = createRover(10, 21, 'N')

    def test_move_f(self):
        r.move(list("f"))
        assert_equal(10, r.x)
        assert_equal(22, r.y)

    def test_move_b(self):
        r.move(list("b"))
        assert_equal(10, r.x)
        assert_equal(20, r.y)

    def test_move_right(self):
        r.move(list('r'))
        assert_equal('E', r.orientation)

    def test_move_left(self):
        r.move(list('l'));
        assert_equals('W', r.orientation)

class TestMovesOrientationSouth:

    def setup(self):
        # tried using self.r, but it gets too wordy using self.r everywhere
        global r
        r = createRover(10, 21, 'S')

    def test_move_forward(self):
        r.move(list("f"))
        assert_equal(10, r.x)
        assert_equal(20, r.y)

    def test_move_backward(self):
        r.move(list("b"))
        assert_equal(10, r.x)
        assert_equal(22, r.y)

    def test_move_right(self):
        r.move(list('r'))
        assert_equal('W', r.orientation)

    def test_move_left(self):
        r.move(list('l'));
        assert_equals('E', r.orientation)

# would love use use test generators!
class TestMovesOrientationEast:

    def setup(self):
        global r
        r = createRover(10, 21, 'E')

    def test_move_forward(self):
        r.move(list('f'))
        assert_equal(11, r.x)
        assert_equal(21, r.y)

    def test_move_backward(self):
        r.move(list("b"))
        assert_equal(9, r.x)
        assert_equal(21, r.y)

    def test_move_right(self):
        r.move(list('r'))
        assert_equal('S', r.orientation)

    def test_move_left(self):
        r.move(list('l'));
        assert_equals('N', r.orientation)

class TestMovesOrientationWest:

    def setup(self):
        global r
        r = createRover(10, 21, 'W')

    def test_move_forward(self):
        r.move(list("f"))
        assert_equals(9, r.x)
        assert_equals(21, r.y)

    def test_move_backward(self):
        r.move(list("b"))
        assert_equal(11, r.x)
        assert_equal(21, r.y)

    def test_move_right(self):
        r.move(list('r'))
        assert_equal('N', r.orientation)

    def test_move_left(self):
        r.move(list('l'));
        assert_equals('S', r.orientation)

class TestMovePath:

    def setup(self):
        global r
        r = createRover(10, 21, 'N')

    def test_simple_path(self):
        r.move(list("ffrff"))
        assert_equal('E', r.orientation)
        assert_equal(12, r.x)
        assert_equal(23, r.y)

class TestWrapping:

    def setup(self):
        global wp
        wp = planet.Planet(3, 3)

    def test_wrap_east_forward(self):
        r = wp.createRover(2, 0, 'E')
        r.move(list("f"))
        assert_equal(0, r.x)

    def test_wrap_west_forward(self):
        r = wp.createRover(0, 0, 'W')
        r.move(list("f"))
        assert_equal(2, r.x)

    def test_wrap_north_forward(self):
        r = wp.createRover(0, 2, 'N')
        r.move(list("f"))
        assert_equal(0, r.y)

    def test_wrap_south_forward(self):
        r = wp.createRover(0, 0, 'S')
        r.move(list("f"))
        assert_equal(2, r.y)

    def test_wrap_east_backward(self):
        r = wp.createRover(0, 0, 'E')
        r.move(list('b'))
        assert_equal(2, r.x)

    def test_wrap_west_backward(self):
        r = wp.createRover(2, 0, 'W')
        r.move(list('b'))
        assert_equal(0, r.x)

    def test_wrap_north_backward(self):
        r = wp.createRover(0, 0, 'N')
        r.move(list('b'))
        assert_equal(2, r.y)

    def test_wrap_south_backward(self):
        r = wp.createRover(0, 2, 'S')
        r.move(list('b'))
        assert_equal(0, r.y)

class TestObstacle:

    def setup(self):
        global p
        p = planet.Planet(20, 20)
        p.setObstacle(10, 12);

    def test_east_forward(self):
        r = p.createRover(9, 12, 'E')
        with assert_raises_regexp(ValueError, "Cannot move to 10,12: obstacle present"):
            r.move(list("f"))

    def test_north_forward(self):
        r = p.createRover(10, 11, 'N')
        with assert_raises_regexp(ValueError, "Cannot move to 10,12: obstacle present"):
            r.move(list("f"))

    def test_west_back(self):
        r = p.createRover(9, 12, 'W')
        with assert_raises_regexp(ValueError, "Cannot move to 10,12: obstacle present"):
            r.move(list("b"))

    def test_path_stops_before(self):
        r = p.createRover(12, 11, 'W')
        with assert_raises_regexp(ValueError, "Cannot move to 10,12: obstacle present"):
            r.move(list("fflb"))
        assert_equal(10, r.x)
        assert_equal(11, r.y)

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

    def test_move_f(self):
        r.move(list("f"))
        assert_equal(22, r.y)
        assert_equal(10, r.x)

    def test_move_b(self):
        r.move(list("b"))
        assert_equal(10, r.x)
        assert_equal(20, r.y)

from nose.tools import *
import rover

def setup():
    global r
    r = rover.Rover(10, 21, 'N')

def test_initial_x():
    assert_equal(10, r.x)
    assert_equal(21, r.y)
    assert_equal('N', r.orientation)

def test_initial_y():
    assert_equal(21, r.y)

def test_initial_orientation():
    assert_equal('N', r.orientation)

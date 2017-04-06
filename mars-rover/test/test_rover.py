from nose.tools import *
import rover

def setup():
    global r
    r = rover.Rover(10, 21, 'N')

def test_initial_x():
    assert_equal(10, r.x)

def test_initial_y():
    assert_equal(21, r.y)

def test_initial_orientation():
    assert_equal('N', r.orientation)

def test_move_f():
    r.move(list("f"))
    assert_equal(22, r.y)
    assert_equal(10, r.x)

@with_setup(setup)
def test_move_b():
    r.move(list("b"))
    assert_equal(10, r.x)
    assert_equal(20, r.y)

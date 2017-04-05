# tdd-python

Learning how to TDD in Python

## other

This uses nose tools

To run:

```nosetests mars-rover -v```

## Links and references

https://www.youtube.com/watch?v=Qw2vczm4m2c&feature=youtu.be

### Nose home page

http://nose.readthedocs.io/en/latest/index.html

Note: nose is a superset of python unittest

This gives three options for installing: easy_setup, pip, download.

On OS X El Capitan and later, SIP issues arise because the installers want to install in the pre-installed
python directory, /Library/Python/2.7/. SIP won't allow even sudo install there.

Well, ``sudo easy_install nose`` eventually worked.
The test runner is at /usr/local/bin/nosetests.

### Nose testing manual

http://nose.readthedocs.io/en/latest/testing.html

## Coding katas

Mars Rover: https://technologyconversations.com/2013/12/29/learning-a-new-programming-language-through-katas-tdd-and-cyberdojo/

## FAQ

Here are some issues I encountered in getting this to work.

## nosetests file not found

After installing nose with pip, cannot find the executable in the path.

Executable should be in /usr/local/bin

Actually the problem is SIP on OS X El Capitan

http://apple.stackexchange.com/questions/209572/how-to-use-pip-after-the-os-x-el-capitan-upgrade

## Mars Rover Kata

https://technologyconversations.com/2013/12/29/learning-a-new-programming-language-through-katas-tdd-and-cyberdojo/

```
Mars Rover Kata.
Taken from http://amirrajan.net/Blog/code-katas-mars-rover

– Develop an api that moves a rover around a grid.
– You are given the initial starting point (x,y) of a rover and the direction (N,S,E,W) it is facing.
– The rover receives a character array of commands.
– Implement commands that move the rover forward/backward (f,b).
– Implement commands that turn the rover left/right (l,r).
– The only commands you can give the rover are f,b,l, and r.
– Implement wrapping from one edge of the grid to another. (planets are spheres after all)
– Implement obstacle detection before each move to a new square. If a given sequence of commands encounters an obstacle, the rover moves up to the last possible point and reports the obstacle.

Here is an example:
– Let’s say that the rover is located at 0,0 facing North on a 100×100 grid.
– Given the command “ffrff” would put the rover at 2,2 facing East.
```

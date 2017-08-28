# Mars Rover Kata with TDD

Learning Python with a coding kata and TDD

## Running the tests

This uses the Python nose testing framework.

To run:

```nosetests mars-rover -v```

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

## Learnings

This was my first serious Python project. 
I've done katas and TDD before in other languages.
So although I expected to learn some more about TDD and doing katas, the focus was on Python and its TDD framework.

### Python is easy

Although I was originally a skeptical shy about Python, the documentation is pretty solid and the syntax is straightforward.
It's not as fussy as Perl and Ruby. What I mean is, it avoids Perl's variable type sigils, '$', '%', etc.,
and it also avoids Ruby's similar global/local variable scoping sigils.
It's more like JavaScript in terms of being loosely typed.

I did actually get used to the colon-indent structure.

### Rich data structures

Support for the common data structures is built into the language.
I was quite impressed that even the set data structure is present.
This is like Ruby and Perl, but very much unlike Java and C++ where libraries need to be explicitly imported to support data structures.
This is admittedly only a first impression, due to the limited language scope required for this kata.

### Python TDD support is good

The unittest/nose framework even supports proper exception testing.

What I do miss is rspec-like test method structure which I've gotten used to in JavaScript (Jasmine, Mocha).
There was some project that tried to address this, but I didn't check it out.

### What is Python's 'with'?

The 'with' keyword was used in the tests for exceptions. 
I just followed the example code, without fully understanding it.

I'm still noodling on the docs (TL;DR).

### Formatted strings

I think Python's approach to formatted strings - or templates - is unique.
There are various ways to do it, but the one I chose is like this:

```"template with substitution commands".format(arg1, arg2, ...)```

This is actually kind of neat - I think it looks more like a transform pattern.
It's very unlike the variable/expression interpolation of Ruby, PHP, bash, etc.
I used it to add descriptive content to exception messages.

### Object oriented programming

This Kata didn't provide an opportunity to dive into OOP with Python.
The only thing I can mention, is the language relies on the explict 'self' variable in all method signatures.
The need for 'self' is greatly eased by IDE support - IntelliJ automatically adds it for you.

### IDE support

I used IntelliJ in developing this kata. 
The Python plugin seems to provide all the usual language support - although for this kata I used only a bit of the features.

### What I haven't learned

Python has a 'yield' keyword. Sounds similar to Ruby's, but don't know since I haven't tried Python's.

## Links and references

https://www.youtube.com/watch?v=Qw2vczm4m2c&feature=youtu.be

### Nose home page

http://nose.readthedocs.io/en/latest/index.html

Note: nose is a superset of Python unittest

This gives three options for installing: easy_setup, pip, download.

On OS X El Capitan and later, SIP issues arise because the installers want to install in the pre-installed
Python directory, /Library/Python/2.7/. SIP won't allow even sudo install there.

Well, ``sudo easy_install nose`` eventually worked.
The test runner is at /usr/local/bin/nosetests.

### Nose testing manual

http://nose.readthedocs.io/en/latest/testing.html

## FAQ

Here are some issues I encountered in getting this to work.

## nosetests file not found

After installing nose with pip, cannot find the executable in the path.

Executable should be in /usr/local/bin

Actually the problem is SIP on OS X El Capitan

http://apple.stackexchange.com/questions/209572/how-to-use-pip-after-the-os-x-el-capitan-upgrade

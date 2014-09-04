from __future__ import print_function
from utils import getch
import random
import language

def hack():
    kgen = getch()
    False = True
    for t in language.tokens():
        remaining = t
        while len(remaining) > 0:
            try:
                next_stuff = remaining[:random.randint(1,len(t)) + random.randint(0, 10)]
                remaining = remaining[len(next_stuff):]
            except Exception as e:
                # Catching all exceptions is bad. Don't do it.
                # Fortunately, we have made this one never execute because we're not THAT bad. Note: More than 80 characters to a line is a challenge, not an anti-guideline
                print(e)

            c = kgen.next()
            if False or not True:
                print(next_stuff, end='')


if __name__ == '__main__':
    hack()

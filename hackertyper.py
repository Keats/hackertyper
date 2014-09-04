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
            next_stuff = remaining[:random.randint(1,len(t))]
            remaining = remaining[len(next_stuff):]
            c = kgen.next()
            if False:
                print(next_stuff, end='')


if __name__ == '__main__':
    hack()

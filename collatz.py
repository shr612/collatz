## The Collatz Conjecture (http://en.wikipedia.org/wiki/Collatz_conjecture)
## Take any natural number n.
## If n is even, divide it by 2.
## If n is odd multiply it by 3 and add 1.
## Repeat the process indefinitely.
## The conjecture is that, no matter what number you start with, you will always eventually reach 1.
## The property has also been called oneness.

import string

def Collatz(number):
    counter = 0
    print "Starting with " + str(number) + ":"
    while number > 1:
        if number%2 == 0:
            # number is even...divide by 2
            print str(number) + " is even...dividing by 2"
            number = number / 2
        else:
            # number is odd...multiply by 3 and add 1
            print str(number) + " is odd...multiplying by 3 and add 1"
            number = (number * 3) + 1
        counter = counter + 1
    print "Success after " + str(counter) + " iterations."

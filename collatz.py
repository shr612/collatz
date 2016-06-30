## The Collatz Conjecture (http://en.wikipedia.org/wiki/Collatz_conjecture)

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

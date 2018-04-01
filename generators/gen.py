# GENERATORS -> eagerness vs laziness

# top-level syntax, function -> underscore method
# x()                           __call__  Called when the instance is 'called' as a function

def add(x, y):
    return x + y

class Adder(object):
    #Although here you can add stateful behaviour 
    def __init__(self, z):
        self.z = z

    def __call__(self, x, y):
        #print "x + y + z" % (x+y+self.z)
        return x + y

add2 = Adder(0)

# Functionality of add and add2 is the same. Behind the scenes their are similiar, sintatically not
# You can think that add() function have some object model that looks like Adder behind it

print add(12, 12)
print add2(12, 12)

print type(add)
print type(add2)

# LONG RUN COMPUTATION - EAGERNESS VS LAZYNESS
from time import sleep

# This method only returns the complete result set of computation in the end. 'Eagerly' returns the complete result all at once. We need to wait to finish to be able to process the first result.
# If we only care about the first value, or first 3 values, we need to wait for the computation to complete
# If we think about it, it takes kinda of 10 units of memory (slots)
# This function always takes the same amount of memory and same amount of time to run
def compute_0():
    result = []
    for i in range(10):
        sleep(.5)
        result.append(i)
    return result

# The next class will have same behaviour as method - nothing gained
"""
class Compute(object):
    def __call__(self):
        result = []
        for i in range(10):
            sleep(.5)
            result.append(i)
        return result

compute = Compute()
"""


# This class still take the same amount of time of computation, but returns each single value
class Compute(object):
    def __call__(self):
        result = []
        for i in range(10):
            sleep(.5)
            result.append(i)
        return result

    def __iter__(self):
        self.last = 0
        return self
    
    # this method return a single value at a time
    def __next__(self):
        rv = self.last
        self.last += 1
        if self.last > 10:
            raise StopIteration        
        sleep(.5)
        return rv

# BEST FORMULATION -> LAZY, NOT EAGER -------------------------------------------------------------------------------------------------------------------------------------------

def compute():
    for i in range(10):
        sleep(.5)
        yield i
        

#for value in Compute():
#    print value

#Calling the lazy method compute()
for value in compute():
    print value
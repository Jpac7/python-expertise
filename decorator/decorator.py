# DECORATOR PATTERN IN PYTHON FUNCTIONS
# developing basic function and adding more functionally to it without refactoring, in runtime


# LIBRARY CODE
from time import time

"""
def timer(func, x, y=0):
    before = time()
    result = func(x,y)
    after = time()
    print 'elapsed:', after - before
    return result
"""
# decorator pattern applied with additional elapsed time calculation for methods
def timer(func):
    # f() is a wrapper function for "func" plus new funcionallities added in it
    # wrapping func with some extra behaviour dinamically
    def f(*args, **kwargs):
        before = time()
        result = func(*args,**kwargs)
        after = time()
        print 'elapsed:', after - before
        return result
    return f

# function with another level that creates the decorator, then the decorator creates the wrapper
# the high-level inserts the number of times (n) the function will be running
def ntimes(n):
    def inner(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                print "{.__name__} iteration".format(func)
                result = func(*args, **kwargs)
            return result
        return wrapper 
    return inner

#@timer  # decorator
@ntimes(2) # running ntimes decorator 2 times
def add(x, y=0):
    return x + y
#add = timer(add) --> applying decorator

#@timer
@ntimes(7)
def sub(x, y=0):
    return x - y
#sub = timer(sub)



# USER CODE
print 'add(10)', add(10)
print 'add(10, 20)', add(10, 20)
print 'add(2, -66)', add(2, -66)
print 'sub(77, 43)', sub(77, 43)

# SEQUENCING AND INTERLEAVING CODE WITH GENERATORS
# RETURN RESULT OR SMALL PART OF THE COMPUTATION AND ALSO CONTROL TO THE CALLER

# First version of API. The user haves to run the method in order 
# for the library not to break, while interleaving between library and user code
# SUBROTINES

class API(object):
    
    def run_this_first(self):
        first()

    def run_this_second(self):
        second()

    def run_this_last(self):
        last()


# Second version of API. Assuring the methods are runned by their order
# and User can interleave his/her code
# CO-ROTINES

def api():
    first()
    yield
    second()
    yield
    last()
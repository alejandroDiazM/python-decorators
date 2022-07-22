#Real world examples of decorated functions
from decorators import timer, debug, slow_down, repeat
import math

@timer
def waste_time(num_times):
    for _ in range(num_times): 
        ([i**2 for i in range(10000)])

# waste_time(1)
# waste_time(1000)

###

@debug
def make_greeting(name, age=None):
    if age is None:
        return f"Hello {name}!"
    return f"Whoa {name}! {age} already!"

# make_greeting("Andrej", 112)

###

math.factorial = debug(math.factorial)

def approximate_e(terms=18):
    return print(sum(1 / math.factorial(n) for n in range(terms)))

# approximate_e(5)

###

@slow_down
def countdown(from_number):
    if from_number < 1:
        print("BOOM!!!")
    else:
        print(from_number)
        countdown(from_number - 1)
    
# countdown(5)

###

#Nested decorators
@debug
@repeat(num_times=4)
def call_hammer(name):
    print(f"Come to me, {name}!")

call_hammer("Mjölnir")

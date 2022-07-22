#Reusing decorators
from decorators import do_twice

@do_twice
def say_hello():
    print("Hello!")

# say_hello()


#Decorating functions with arguments
@do_twice
def greet(name):
    print(f"Hello {name}!")

# greet("Guido")


#Returning values from decorated functions
@do_twice
def return_greeting(name):
    print("Creating greeting.")
    return f"Hi {name}"

hi_guido = return_greeting("Guido")
print(hi_guido)

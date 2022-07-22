#First class functions
def say_hello(name):
    print(f"Hello {name}!")

def be_awesome(name):
    print(f"{name} is awesome!")

def greet_guido(greeter_func):
    return greeter_func("Guido")

# greet_guido(say_hello)
# greet_guido(be_awesome)


#Inner functions
def parent():
    print("Printing from the parent() function.")

    def first_child():
        print("Printing from the first_child() function.")

    def second_child():
        print("Printing from the second_child() function.")

    second_child()
    first_child()

# parent()


#Functions as return values
def parent(num):
    def first_child():
        print("Hi, I am Emma.")

    def second_child():
        print("Hi, I am Liam.")
    
    if num == 1:
        return first_child
    return second_child

first = parent(1)
second = parent(2)

# first()
# second()


#Simple decorator
def my_decorator(func):
    def wrapper():
        print("Before.")
        func()
        print("After.")
    return wrapper

def say_hello():
    print("Hello!")

say_hello = my_decorator(say_hello)

# say_hello()


#Behaviour changing decorator
from datetime import datetime

def not_during_night(func):
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            func()
        print("Shhhhh!")
    return wrapper

def scream():
    print("Hey!!!")

scream = not_during_night(scream)

# scream()


#Simpler sintax with @
def my_decorator(func):
    def wrapper():
        print("Before.")
        func()
        print("After.")
    return wrapper

@my_decorator #vs say_hello = my_decorator(say_hello)
def say_hello():
    print("Hello.")

say_hello()

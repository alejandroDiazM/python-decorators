import random
PLUGINS = dict()

def register(func):
    PLUGINS[func.__name__] = func
    return func

@register
def say_hello(name):
    print(f"Hello, {name}.")

@register
def obi_wan(name):
    print(f"Hello there, {name}.")

def random_greet(name):
    greeter, greeter_func = random.choice(list(PLUGINS.items()))
    print(f"Using {greeter!r}")
    return greeter_func(name)

random_greet("Luke")
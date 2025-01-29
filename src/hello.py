
def say_hello(name):
    return "hello " + name

def add(a, b):
    return a + b


# ---- tests ---- #

def test_say_hello():
    assert say_hello("Luke") == "hello Luke"
    assert say_hello("Neil") == "hello Neil"

def test_add():
    assert add(1, 1) == 2
    
def test_add_negatives():
    assert add(-2, -2) == -4
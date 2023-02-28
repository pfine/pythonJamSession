"""
From: https://www.youtube.com/watch?v=6tNS--WetLI&t=1102s
Python Tutorial: Unit Testing Your Code with the unittest Module
"""
def add(x, y):
    """Add + function"""
    return x + y

def substract(x, y):
    """Substract - function"""
    return x - y

def multiply(x, y):
    """Multiplay * function"""
    return x * y

def divide(x, y):
    """Divide / function"""
    if y == 0:
        raise ('Can not divide by zerp (0) !!!')
    return x / y

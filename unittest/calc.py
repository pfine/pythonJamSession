"""
From: https://www.youtube.com/watch?v=6tNS--WetLI&t=1102s
Python Tutorial: Unit Testing Your Code with the unittest Module
"""
def add(x, y):
    """Add + function"""
    return x + y

def subtract(x, y):
    """Subtract - function"""
    return x - y

def multiply(x, y):
    """Multiply * function"""
    return x * y

def divide(x, y):
    """Divide / function"""
    if y == 0:
        raise ValueError('Can not divide by zero (0) !!!')
    return x / y

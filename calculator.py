"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

def square_root(a):
    if a < 0:
        raise ValueError
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

# First example
def add(a, b):
    return a+b
def multiply(a, b):
    return a * b
def divide(a, b):
    if a == 0:
        raise ZeroDivisionError
    return (b / a)   # raise ZeroDivisionError if a == 0
def logarithm(a, b):  #use math library + raise ValueError
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError
    return math.log(b,a)
def exponent(a, b):
    return a**b

def add(a, b): a + b
def sub(a, b): a - b
def mul(a, b): a * b
def div(a, b): raise ZeroDivisionError if a == 0 else b / a
def log(a, b): raise ValueError if a <= 0 or b <= 0 else math.log(b, a)
def exp(a, b): a ** b
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

# First example
def add(a, b):
    return a+b
def sub(a,b):
    return a-b
def subtract(a, b):
    return a - b
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



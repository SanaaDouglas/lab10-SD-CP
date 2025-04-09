"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

def add(a, b): a + b
def subtract(a, b): a - b
def multiply(a, b): a * b
def divide(a, b): raise ZeroDivisionError if a == 0 else b / a
def logarithm(a, b): raise ValueError if a <= 0 or b <= 0 else math.log(b, a)
def exp(a, b): a ** b
#!/usr/bin/python3
"""
add_integer:
    Checks if parameters are int
    Returns sum of parameters
"""
import math


def add_integer(a, b=98):
    """
    Checks if int or float (but not bool), convert floats to int, otherwise raise.
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    if type(a) is float:
        if math.isnan(a):
            raise ValueError("cannot convert float NaN to integer")
        a = int(a)
    if type(b) is float:
        if math.isnan(b):
            raise ValueError("cannot convert float NaN to integer")
        b = int(b)

    return a + b

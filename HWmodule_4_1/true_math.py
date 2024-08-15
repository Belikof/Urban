import math


def divide(first, second):
    divide_infinity = math.inf if second == 0 else first / second
    return divide_infinity

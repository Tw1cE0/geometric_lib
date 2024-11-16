import math

def area(r):
    if r < 0:
        raise ValueError("Radius must be non-negative")
    return math.pi * r ** 2

def perimeter(r):
    if r < 0:
        raise ValueError("Radius must be non-negative")
    return 2 * math.pi * r


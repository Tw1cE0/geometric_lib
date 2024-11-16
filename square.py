
def area(a):
    if a < 0:
        raise ValueError("Side must be non-negative")
    return a * a


def perimeter(a):
    if a < 0:
        raise ValueError("Side must be non-negative")
    return 4 * a

import math

def area(r):
    """
    Возвращает площадь круга.

    Args:
        r (float): Радиус круга.

    Returns:
        float: Площадь круга.

    Example:
        >>> area(5)
        78.53981633974483
    """
    return math.pi * r * r

def perimeter(r):
    """
    Возвращает периметр круга.

    Args:
        r (float): Радиус круга.

    Returns:
        float: Периметр круга.

    Example:
        >>> perimeter(5)
        31.41592653589793
    """
    return 2 * math.pi * r

import math

def area(r):
    if not isinstance(r, (int, float)):
        raise TypeError("The radius of the circle must be a number")

    if (r >= 0):
        return math.pi * r * r

    raise ValueError("The radius of the circle must be non-negative")


def perimeter(r):
    if not isinstance(r, (int, float)):
        raise TypeError("The radius of the circle must be a number")

    if (r >= 0):
        return 2 * math.pi * r

    raise ValueError("The radius of the circle must be non-negative")
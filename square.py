def area(a):
    if not isinstance(a, (int, float)):
        raise TypeError("The sides of the square must be a number")

    if a >= 0:
        return a * a

    raise ValueError("The sides of the square must be non-negative")


def perimeter(a):
    if not isinstance(a, (int, float)):
        raise TypeError("The sides of the square must be a number")

    if a >= 0:
        return 4 * a

    raise ValueError("The sides of the square must be non-negative")
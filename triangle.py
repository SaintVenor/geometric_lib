def area(a, h):
    if not isinstance(a, (int, float)) or not isinstance(h, (int, float)):
        raise TypeError("The sides and height of the triangle must be a number")

    if a >= 0 and h >= 0:
        return a * h / 2

    raise ValueError("The sides and height of the triangle must be non-negative")


def perimeter(a, b, c):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
        raise TypeError("The sides of the triangle must be a number")

    if a >= 0 and b >= 0 and c >= 0:
        return a + b + c

    raise ValueError("The sides of the triangle must be non-negative")


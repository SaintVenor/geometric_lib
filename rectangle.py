def area(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("The sides of the rectangle must be a number")

    if a >= 0 and b >= 0:
        return a * b

    raise ValueError("The sides of the rectangle must be non-negative")



def perimeter(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("The sides of the rectangle must be a number")

    if a >= 0 and b >= 0:
        return (a + b) * 2

    raise ValueError("The sides of the rectangle must be non-negative")
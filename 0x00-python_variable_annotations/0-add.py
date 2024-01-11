#!/usr/bin/env python3

def add(a: float, b: float) -> float:
    """
    Adds two float numbers and returns their sum.

    :param a: The first float number.
    :param b: The second float number.
    :return: The sum of a and b.
    """
    return a + b


if __name__ == "__main__":
    print(add(1.11, 2.22) == 1.11 + 2.22)
    print(add.__annotations__)

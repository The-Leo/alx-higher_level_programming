#!/usr/bin/python3
"""

This module is comprises a function that adds two numbers

"""

def add_integer(a, b=98):
        """This function adds two integers and/or float numbers

    Parameters:
        a: first number
        b: second number

    Returns:
        The addition of the two given numbers

    Raises:
        TypeError: If a or b are not integers and/or float numbers

    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)

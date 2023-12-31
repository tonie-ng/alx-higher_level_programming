#!/usr/bin/python3

"""Defines a Square class."""


class Square:
    """A Square class."""

    def __init__(self, size=0):
        """Initializes attributes of a square class

        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    """Calculates the area of the sqaure

    Returns:
        the area of the square
    """
    def area(self):
        area = self.__size * self.__size
        return (area)

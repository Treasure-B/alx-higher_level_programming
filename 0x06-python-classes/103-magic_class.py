#!/usr/bin/python3
"""
MagicClass Class Definition.
"""


import math


class MagicClass:
    """
    Represent a circle.

    Attributes:
        __radius (float): The radius of the circle.
    """

    def __init__(self, radius=0):
        """
        Initialize a new MagicClass instance.

        Args:
            radius (float or int): The radius of the circle. Default is 0.

        Raises:
            TypeError: If the radius is not a number.
        """
        self.__radius = 0
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """
        Calculate and return the area of the MagicClass.

        Returns:
            float: The calculated area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculate and return the circumference of the MagicClass.

        Returns:
            float: The calculated circumference of the circle.
        """
        return 2 * math.pi * self.__radius

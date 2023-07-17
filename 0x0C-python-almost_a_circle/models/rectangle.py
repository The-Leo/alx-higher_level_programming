#!/usr/bin/python3
"""
    contains class Rectangle which implements Base.
"""
from models.base import Base


class Rectangle(Base):
    """
        class Rectangle implements Base.
        Methods:
            __init__()
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
            Initializes the instance of the class..
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

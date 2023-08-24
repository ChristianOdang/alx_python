""" 
Write a class Rectangle that inherit from BaseGeometry
"""
Rectangle = __import__('-rectangle').Rectangle


class Square(Rectangle):
    """ 
    A class define for square that inherit Rectangle
    """

    def __init__(self, size):
        """ 
        Initialization method for class Square
        """
        Rectangle.integer_validator(self, "size", size)
        self.__size = size

    def area(self):
        """ 
        Method to calculate area
        """
        return self.__size ** 2

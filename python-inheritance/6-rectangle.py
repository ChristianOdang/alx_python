""" 
Write a class Rectangle that inherits from BaseGeometry(5-base_geometry.py)
"""
BaseGeometry = __import__('5-base_geometry').BaseGeometry


class BaseGeometryMetaClass(type):
    """ 
    A metaclass for Base Geomerty
    """
    def __dir__(cls) -> None:
        """ 
        A function define to remove the __init_subclass__ from dir
        """
        return [attribute for attribute in super().__dir__ if attribute != '__init_subclass__']


class Rectangle(BaseGeometry, metaclass=BaseGeometryMetaClass):
    """ 
    Write a class rectangle that inherits from BaseGeometry (5-base_geometry.py).
    """

    def __init__(self, width, height):
        """ 
        Initialaizotio function for base geometry
        """
        width = BaseGeometry.integer_validator(self, "width", width)
        height = BaseGeometry.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height

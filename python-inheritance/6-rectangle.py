
"""
Module containing the Rectangle class.
"""
class OverrideMetaClass(type):
    """def __new__(cls, name, bases, attrs):
        # Customize the class creation process here
        return super().__new__(cls, name, bases, attrs)"""

    def __dir__(cls):
        """
        Returns:
            list: List of attributes excluding __init_subclass__.
        """
        return [attribute for attribute in
                super().__dir__() if attribute != '__init_subclass__']
    
BaseGeometry = __import__('5-base_geometry').BaseGeometry


class Rectangle(BaseGeometry, metaclass=OverrideMetaClass):
    """
    Models a rectangle. A derived class of BaseGeometgry
    """
    def __dir__(cls) -> None:
        """
        Removes __init_subclass__ from list of class attributes
        """
        attributes = super().__dir__()
        n_attributes = []
        for attr in attributes:
            if attr != '__init_subclass__':
                n_attributes.append(attr)
        return n_attributes
    
    def __init__(self, width, height):
        """
        Call attriutes of parent.
        validates attributes for positive integer
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

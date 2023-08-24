""" 
The module of a class name Geometry that has a single function
"""


class BaseGeometry:
    """ 
    This method check if a class is an instance of the define object
    example 1 is an instance of the class int
    """
    def __dir__(cls) -> None:
        """ 
        This method check if a class is an instance of the define object
        example 1 is an instance of the class in
        """
        attrib = super().__dir__()
        n_attri = []
        for attr in attrib:
            if attr != '__init_subclass__':
                n_attri.append(attr)
        return n_attri

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name: str, value: int):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

""" 
The module of a class name BaseGeometry
"""


class BaseGeometery:
    """ 
    This method check if a class is an instance of the define object
    example 1 is an instance of the class int
    """

    def __dir__(cls) -> None:
        """ 
        The function overide the default __dir__ function
        """
        attrib = super().__dir__()
        n_attri = []
        for attr in attrib:
            if attr != '__init_subclass__':
                n_attri.append(attr)
        return n_attri

    def area(self):
        """ 
        This function raise an error if the area method is not define
        """
        raise Exception("area() is not implemented")

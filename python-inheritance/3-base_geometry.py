""" A function that returns True if class instanceof or a subclass is the same
"""


class BaseGeometrytryMetaClass(type):
    """ A metaclass for Base Geometry
    """
    def __dir__(cls) -> None:
        """ 
        A Function define to remove the __init_subclass__ from dir
        """
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']


class BaseGeometry(metaclass=BaseGeometrytryMetaClass):
    """ 
    This method check if a class is an instance of the define object
    """

    def __dir__(cls) -> None:

        attrib = super().__dir__()
        n_attri = []
        for attr in attrib:
            if attr != '__init_subclass__':
                n_attri.append(attr)
        return n_attri

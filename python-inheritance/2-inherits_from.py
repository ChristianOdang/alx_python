""" 
This Module is issubclass method takes the obj type variable,
and a_class method
"""


def is_kind_class(obj, a_class):
    """ 
    Function to check if obj is an instance of class
    Args:
         obj ([type]): object
         a_class ([type]): a class
         
    Returns:
        True: obj ia an instance of a_class
        False: obj not an instance of a a_class

    """
    # if isinstance(type(obj), a_class)
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False

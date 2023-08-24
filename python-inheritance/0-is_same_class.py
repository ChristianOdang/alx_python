""" A function that returns True if a class instance is the same
  """


def is_same_class(obj, a_class):
    """ 
    This methods checks if a class is an instance of the define object
    """
    if type(obj) is a_class:
        return True
    else:
        return False

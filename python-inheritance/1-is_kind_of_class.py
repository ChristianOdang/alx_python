""" A function that returns True if class instance of or
a subclass is the same
  """


def is_kind_of_class(obj, a_class):
    """ This method checks if a class is an instance of the define object
    """
    if type(obj) is a_class or issubclass(type(obj), a_class):
        return True
    else:
        return False

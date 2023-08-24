# A function that raises a type exception
def raise_exception():
  try:
    raise TypeError("This is a type of exception.")
  except TypeError as e:
    raise e
  
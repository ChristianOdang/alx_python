"""Write a class Square that defines a square by
Private instance attribute size and Instantation with optional size 
  """
class Square:
  """This method initialize a square method and check
  if the value is of type int or less than 0
  """
  def __init__(self, size=0):
      if type(size) != int:
         raise TypeError("size must be an integer")
      if size < 0:
         raise ValueError("size must be >= 0")
      self.__size = size 

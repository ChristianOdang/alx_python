"""Module to calculate the area of a square
  """
class Square:
  """this class uses the getter to return the area from
  the square method
  """
  def __init__(self, size=0):
    if type(size) != int:
      raise TypeError("size must be an integer")
    if size < 0:
      raise ValueError("size must be >= 0")
    self.__size = size 
    
  def area(self):
    area = self.__size ** 2
    return area
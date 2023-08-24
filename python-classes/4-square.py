"""Module calculate the area of a square
  """
class Square:
  """ This class uses the getter to return the area from
  the square method
  """
  def __init__(self, size=0):
    self.__size = size
    
  @property
  def size(self):
    return self.__size
  
  @size.getter
  def size(self, value):
    if type(value) != int:
      raise TypeError("size must be an integer")
    elif value < 0:
      raise ValueError("size must be >= 0")
    else:
      self.__size = value
      return self.__size
    
  def get_size(self):
      return self.__size
    
  def area(self):
      return self.__size ** 2
    
  def my_print(self):
      area = self.__size
      if area != 0:
        for i in range(0, area):
          for j in range(0, area - 1):
            print("#", end='')
          print("#")
      else:
        print()

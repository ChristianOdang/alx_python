""" This is a module that implement the base required for 
for other Class in Python
"""


class Base:
    '''A base class for Python just a circle.
       the goal of the base class will be to manage id in all projects
    '''

    # create a class attribute to hold the count
    __nb_objects = 0

    def __init__(self, id: int = None):
        ''' 
        Function instantiation for base class

          Parameter:
             id: integer, default value = None

          Returns:
             increment self.id if id is none otherwise self id = id
        '''

        Base.__nb_objects += 1

        if id != None:
            self.id = id
        else:
            self.id = Base.__nb_objects

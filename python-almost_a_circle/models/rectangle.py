'''
    This is the first Rectangle that 
    inherits from Base Module
'''
from models.base import Base
# from base import Base


class Rectangle(Base):
    '''
    Definition:
        A class defition for Rectangle that takes private param,
        and initiialize using a constructior
    Inheritance:
        inherit from Base class.
    '''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''
        Class construtuctor for the clas rectangle

        Parameters:
            width: supplied at instatiation
            height: supplied at instatiation
            x:  default = 0
            y:  default = 0
            id: default = None, inherited from Base class
        Return:
            The return param will be

        '''
        # validate each param
        self.validation('width', width)
        self.validation('height', height)
        self.validation('x', x)
        self.validation('y', y)

        # set each param after validation
        self._Rectangle__width = width
        self._Rectangle__height = height
        self._Rectangle__x = x
        self._Rectangle__y = y
        super().__init__(id)

    def __str__(self):
        '''
        The string method takes the object and return a readable
        format 
        '''
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self._Rectangle__x, self._Rectangle__y, self._Rectangle__width,
                                                       self._Rectangle__height)

    #   @property decorator. This method allows us to
    #   access the private attribute as if it
    #   were a regular attribute, using obj.private_attribute

    @property
    def Rectangle__width(self):
        '''
        Return:
            return the width param from the private property
        '''
        return self._Rectangle__width

    #    This method allows us to set the private attribute's
    #    value with validation or additional logic
    @Rectangle__width.setter
    def Rectangle__width(self, width):
        '''
        Return:
           Set the width private property attributes field.
        '''
        self.validation('width', width)
        self._Rectangle__width = width

    @property
    def width(self):
        '''
        Return:
            return the width param from the private property
        '''
        return self._Rectangle__width

    @width.setter
    def width(self, width):
        '''
        Return:
           Set the width private property attributes field.
        '''
        self.validation('width', width)
        self._Rectangle__width = width

    @property
    def Rectangle__height(self):
        '''
        Return:
            return the height param from the private property
        '''
        return self._Rectangle__height

    @Rectangle__height.setter
    def Rectangle__height(self, height):
        '''
        Return:
           Set the height private property attributes field.
        '''
        self.validation('height', height)
        self._Rectangle__height = height

    @property
    def height(self):
        '''
        Return:
            return the height param from the private property
        '''
        return self._Rectangle__height

    @height.setter
    def height(self, height):
        '''
        Return:
           Set the height private property attributes field.
        '''
        self.validation('height', height)
        self._Rectangle__height = height

    @property
    def Rectangle__x(self):
        '''
        Return:
            return the x param from the private property
        '''
        return self._Rectangle__x

    @Rectangle__x.setter
    def Rectangle__x(self, x):
        '''
        Return:
           Set the x private property attributes field.
        '''
        self.validation('x', x)
        self._Rectangle__x = x

    @property
    def x(self):
        '''
        Return:
            return the x param from the private property
        '''
        return self._Rectangle__x

    @x.setter
    def x(self, x):
        '''
        Return:
           Set the x private property attributes field.
        '''
        self.validation('x', x)
        self._Rectangle__x = x

    @property
    def Rectangle__y(self):
        '''
        Return:
            return the x param from the private property
        '''
        return self.__y

    @Rectangle__y.setter
    def Rectangle__y(self, y):
        '''
        Return:
           Set the y private property attributes field.
        '''
        self.validation('y', y)
        self._Rectangle__y = y

    @property
    def y(self):
        '''
        Return:
            return the y param from the private property
        '''
        return self._Rectangle__y

    @y.setter
    def y(self, y):
        '''
        Return:
           Set the y private property attributes field.
        '''
        self.validation('y', y)
        self._Rectangle__y = y

    #   validation class for Rectangle

    def validation(self, name: str, param: int):
        '''
        Validation method 

        Parameters:
            Name: str name of param to be vailidated. example x
            Param: int, the value to be valitade must be int at
            all time
        Return:
            exception: Typeerror, ValueError or Pass if test is 
            successful
        '''
        if (type(param) != int):
            raise TypeError("{} must be an integer".format(name))
        elif (type(name) != str):
            raise ValueError("{} name must be a str".format(name))
        elif (name not in ['x', 'y']):
            if (param <= 0):
                raise ValueError("{} must be > 0".format(name))
        elif (name == 'x' or name == 'y'):
            if (param < 0):
                raise ValueError("{} must be >= 0".format(name))

    #   Area calculatore for Rectangle class

    def area(self):
        '''
        THis method return the area of the the rectangle
        PArameters:
            self
        Return:
            the prpduct of height and width
        '''
        return self._Rectangle__height * self._Rectangle__width

    #  Display method for python class Rectangle

    def display(self):
        '''
        This function return a square matrix of # for anyinput of x and y

        Paramter:
            self:
        Return:
            square matrix of #
        '''
        width = self._Rectangle__width
        height = self._Rectangle__height
        x = self.Rectangle__x
        y = self.Rectangle__y

        # print a square matrix from x and y
        for i in range(y):  # write the top space
            print("" * y, end='\n')
        for i in range(height):  # row
            for j in range(x):  # write the column white space
                print(" ", end='')
            for j in range(width-1):  # column
                print("#", end="")
            print("#")

        #   Update for class python
    def update(self, *args, **kwargs):
        '''
        This function return a square matrix of # for anyinput of x and y

        Paramter:
            self:
        Return:
            square matrix of #
        '''
        if args:
            for arg in args:
                self.id = arg
                self._Rectangle__width = arg
                self._Rectangle__height = arg
                self._Rectangle__x = arg
                self._Rectangle__y = arg
        else:
            for key, value in kwargs.items():
                self.id = kwargs.get('id') if 'id' in kwargs else self.id
                self._Rectangle__x = kwargs.get(
                    'x') if 'x' in kwargs else self.Rectangle__x
                self._Rectangle__y = kwargs.get(
                    'y') if 'y' in kwargs else self.Rectangle__y
                self._Rectangle__width = kwargs.get(
                    'width') if 'width' in kwargs else self.Rectangle__width
                self._Rectangle__height = kwargs.get(
                    'height') if 'height' in kwargs else self.Rectangle__height

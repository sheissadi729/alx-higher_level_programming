#!/usr/bin/python3
"""defines a rectangle"""


class Rectangle:
    """represent a rectangle"""
    number_of_instances = 0
    def __init__(self, width=0, height=0):
        """initialize a new rectangle"""
        self.width = width
        self.height = height 
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """ print the rectangle with the character #"""
        if self.__width == 0 or self.__height == 0:
            return ""
        str_list = []
        for i in range(self.__height):
            for j in range(self.__width):
                str_list.append("#")
            if i != self.__height - 1:
                str_list.append("\n")
        return "".join(str_list)

    def __repr__(self):
        """return a string representation of the rectangle
        to be able to recreate a new instance by using eval()"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """prints something when an object is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

class shapes :
    def __init__(self, name, side):
        self.name = name
        self.side = side
    def Area(self) :
        print("I am a :" + self.name +"\n" +
              "I have " + self.side + "sides")
        obj_shape = shapes("shape", "so many")
        obj_shape.Area()

class Rectangle(shapes):
    def __init__(self, len1, wid1):
        self.length = len1
        self.width = wid1

    def Area(self):
        result = self.length * self.width
        return result
obj_book = Rectangle(10, 7)
obj_screen = Rectangle(5, 7)
print("The area of a book is " + str(obj_book.Area()))
print("The area of a screen is " + str(obj_screen.Area()))


class Circle(shapes):
    def __init__(self, rad):
        self.radius = rad
        import math
        self.pi = math.pi

    def Area(self):
        result = self.pi * self.radius ** 2
        return result


obj_circle = Circle(3)
print("The area of a circle is " + str(round(obj_circle.Area(),2)))

class Triangle(shapes):
    def __init__(self, base, height):
        self.Base = base
        self.Height = height

    def Area(self):
        result = ((0.5 * self.Base) * self.Height)
        return result

obj_tri = Triangle(5, 2)
print("The area of a triangle is " + str(obj_tri.Area()))








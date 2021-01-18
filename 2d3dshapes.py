"""
Author: Pang Jin Jia
Last updated: 18 Jan 2021
"""
import math

class Square:
    def __init__(self,length):
        """
        Arguments
        Square(length)
        """
        self.length = length
        
    def area(self):
        a = self.length**2
        print(f"Area of square is: {a:.2f} cm\u00b2")
        
    def perimeter(self):
        p = self.length*4
        print(f"Perimeter of square is: {p:.2f} cm")

class Rectangle:
    def __init__(self,length,breadth):
        """
        Arguments
        Rectangle(length,breadth)
        """
        self.length = length
        self.breadth = breadth
        
    def area(self):
        a = self.length*self.breadth
        print(f"Area of rectangle is: {a:.2f} cm\u00b2")
        
    def perimeter(self):
        p = self.length*2 + self.breadth*2
        print(f"Perimeter of rectangle is: {p:.2f} cm")

class Triangle:
    def __init__(self,base,height):
        """
        Arguments
        Triangle(base,height)
        """
        self.base = base
        self.height = height
        
    def area(self):
        a = self.base*self.height*0.5
        print(f"Area of triangle is: {a:.2f} cm\u00b2")
        
class EquilateralTriangle:
        """
        Arguments
        EquilateralTriangle(sidelength)
        """
    def __init__(self,sidelength):
        self.length = sidelength
        
    def height(self):
        h = (math.sqrt(3)/2)*self.length
        print(f"Height of equilateral triangle is: {h:.2f} cm")
    
    def area(self):
        a = (math.sqrt(3)/4)*self.length
        print(f"Area of equilateral triangle is: {a:.2f} cm")

class Parallelogram:
    def __init__(self,base,height,length,breadth):
        """
        Arguments
        Parallelogram(base,height,length,breadth)
        """
        self.base = base
        self.height = height
        self.length = length
        self.breadth = breadth
    
    def area(self):
        a = base*height
        print(f"Area of parallelogram is: {a:.2f} cm\u00b2")
        
    def perimeter(self):
        p = (self.length*2)+(self.breadth*2)
        print(f"Perimeter of parallelogram is: {p:.2f} cm")

class Trapezoid:
    def __init__(self,height,para1,para2,side1,side2):
        """
        Arguments
        Trapezoid(height,shortParallelLine,longParallelLine,side1,side2)
        """
        self.height = height
        self.para1 = para1
        self.para2 = para2
        self.side1 = side1
        self.side2 = side2
        
    def area(self):
        a = 0.5*(self.para1 + self.para2)*height
        print(f"Area of trapezoid is: {a:.2f} cm\u00b2")
        
    def perimeter(self):
        p = self.para1 + self.para2 + self.side1 + self.side2
        print(f"Perimeter of trapezoid is: {p:.2f} cm")

class Circle:
    def __init__(self,radius):
        """
        Arguments
        Circle(radius)
        """
        self.radius = radius
    
    def diameter(self):
        d = self.radius*2
        print(f"Diameter of circle is: {d:.2f} cm")

    def area(self):
        a = self.radius**2*math.pi
        print(f"Area of circle is: {a:.2f} cm\u00b2")
        
    def circumference(self):
        c = self.radius*2*math.pi
        print(f"Circumference of circle is: {c:.2f} cm")

class SectorOfCircle:
    def __init__(self,radius,degrees):
        """
        Arguments
        SectorOfCircle(radius,degrees)
        """
        self.radius = radius
        self.radian = math.radians(degrees)
        
    def area(self):
        a = 0.5*self.radian*self.radius**2
        print(f"Area of sector of circle is: {a:.2f} cm\u00b2")
        
    def arcLength(self):
        a = self.radian*self.radius
        print(f"Arc length of sector of circle is: {a:.2f} cm")
        
class Ellipse:
    def __init__(self,major,minor):
        """
        Arguments
        Ellipse(semimajor axis, semiminor axis)
        """
        self.major = major
        self.minor = minor        
        
    def area(self):
        a = math.pi*self.major*self.minor
        print(f"Area of ellipse is: {a:.2f} cm\u00b2")
        
    def circumference(self):
        c = math.pi*(3*(self.major+self.minor) - sqrt((self.major+3*self.minor)(3*self.major+self.minor)))
        print(f"Circumference of ellipse is: {c:.2f} cm")
        
class Cone:
    def __init__(self,radius,height):
        """
        Arguments
        Cone(radius, height)
        """
        self.radius = radius
        self.height = height
        
    def volume(self):
        v = self.radius**2*math.pi*self.height*(1/3)
        print(f"Volume of cone is: {v:.2f} cm\u00b3")

class Cylinder:
    def __init__(self,radius,height):
        """
        Arguments
        Cylinder(radius, height)
        """
        self.radius = radius
        self.height = height
        
    def volume(self):
        v = self.radius**2*math.pi*self.height
        print(f"Volume of cone is: {v:.2f} cm\u00b3")
        
    def surfaceArea(self):
        sa = 2*(self.radius**2*math.pi) + 2*self.radius*math.pi*height
        print(f"Surface area of cone is: {sa:.2f} cm\u00b2")
        
class Sphere:
    def __init__(self,radius):
        """
        Arguments
        Sphere(radius)
        """
        self.radius = radius

    def volume(self):
        v = self.radius**3*math.pi*(4/3)
        print(f"Volume of sphere is: {v:.2f} cm\u00b3")
        

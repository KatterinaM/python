from math import sqrt, pi


class Line:

    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def slope(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return (y2 - y1) / (x2 - x1)

coordinate1 = (3, 2)
coordinate2 = (8, 10)

li = Line(coordinate1, coordinate2)
print(li.distance())
print(li.slope())


class Cylinder:

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        result  = pi * self.radius ** 2 * self.height
        return round(result, 2)


    def surface_area(self):
        lateral_area = 2 * pi * self.radius * self.height
        base_area = 2 * pi * self.radius ** 2
        return round(lateral_area + base_area, 2)


c = Cylinder(2,3)
print(c.volume())
print(c.surface_area())
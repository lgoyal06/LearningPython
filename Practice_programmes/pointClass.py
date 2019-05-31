import math
class Point:
    def __init__(self,x, y, z):
        self.x=x
        self.y=y
        self.z=z
    def __str__(self):
       	return ', '.join(['{key}={value}'.format(key=key, value=self.__dict__.get(key)) for key in self.__dict__])

def distance(point1, point2):
  xdiff = point2.x-point1.x
  ydiff = point2.y-point1.y
  zdiff = point2.z-point1.z
  dist = math.sqrt(xdiff**2 + ydiff**2+ zdiff**2)
  return dist
        
p1 = Point(4, 5, 6) 
p2 = Point(-2, -1, 4)
print(distance(p1,p2))

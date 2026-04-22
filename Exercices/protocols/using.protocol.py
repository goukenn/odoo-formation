from abc import abstractmethod
import math
import string
from typing import Protocol
 
class LocalProtocol(Protocol):
    def send(name:string):pass

class BaseImpl(LocalProtocol):
    pass

class Figure(Protocol):
    # define abstract method 
    @abstractmethod
    def area(self) -> None : ...
 
class Rectangle(Figure):
    pass

class RectShape(Rectangle):
    def area(self):
        pass
    
class Vector2f:
    def __init__(self, x, y):
        self.x = x
        self.y = y 

    def __str__(self):
        return f'{self.x}x{self.y}'
    
class CircleShape(Rectangle):
    def __init__(self, center: Vector2f, radius=0):
        super().__init__()
        self.center = center
        self.radius = radius
    
    def area(self):
        return 2 * math.pi * self.radius


print('runtime - check')
c = CircleShape(Vector2f(0, 0), 50)

print('area: ', c.area())

print('data base')
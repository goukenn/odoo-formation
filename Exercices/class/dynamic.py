import sys
import types

def callback(self, *logic):
    print('invoke logic', self, logic)
class Info:
    # __slots__ = ['callback', 'doaction']
    def __init__(self):
        self.x = 0
        self.y, self.z = 0,0

    def __getattr__(self, name: str):
        fc = 'get' + name.capitalize()
        cl = self.__class__
        nf = None
        if (hasattr(cl, fc)):
            nf = getattr(self, fc) # retrieve attribugte attached to an instance
            if callable(nf):
                return nf() # call instance method 
            
    def __setattr__(self, name, value):
        fc = 'set' + name.capitalize()
        cl = self.__class__
        if hasattr(cl, fc):
            nf = getattr(self, fc) 
            if callable(nf):
                return nf(*[value])
        super().__setattr__(name, value)

    def getName(self):
        return f'name: :<- {self}'
    
    def setT(self, value):
        self.__dict__['::t'] = value

    def getT(self):
        return self.__dict__.get('::t')
a = Info()
b = a
print(a.name)
# a.t = 888
print(a.__dict__, a.__sizeof__(), sys.getsizeof(a))
sys.exit()


# we can affet an lambda expression 
a.doaction = lambda self, s: f'{self}' + s
a.doaction = types.MethodType(callback, a)
setattr(a, 'name', 'C.A.D')

delattr(a, 'name')
print(a.name)

print(a.doaction(45))

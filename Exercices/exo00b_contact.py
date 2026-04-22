class Book:
    def __init__(self, a: int):
        self.amount = a

    def __str__(self):
        return str(self.amount)
    
    def __repr__(self):
        return f'the data {self.amount!r}'
 

# **NOTE:** !r quote string inf format.


x = Book("100")
    
y = "55" + str(x) 
    
print( x, repr(x) , str(x))
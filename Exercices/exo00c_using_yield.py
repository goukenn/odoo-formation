class marchand:
    def doAction(self): 
        for i in self.list:
            yield i  

    def __init__(self):
        self.list = [1 ,2 ,5 ]
        self.index = 0

    
m = marchand()

po = m.doAction();

while(not po is None):
    try:
        print('next: ======== ',  next(po))
    except:
        po = None
   

# delete my decorator ....


import inspect
def my_decorator(func):
    def cldef():
        print('create class instance ')
        func.prompt = '> igkdev prompt $'
        return func()
    if inspect.isclass(func): 
        return cldef

    def _warp_call():
        print('calling definition')
        func()
        print('after calling')
    return _warp_call # change de function call


# @my_decorator
def entry_point():
    print('entry point')

@my_decorator
class app:
    def __init__(self):
        self.init = True
    def __str__(self) -> str :
        return "application setting"

entry_point()

_n = app()
print(_n.prompt)
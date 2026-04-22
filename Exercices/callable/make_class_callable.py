class InvokeCallbackClass:

    def __call__(self, *args, **kwds):
        """
        This is how we make a class callable
        """
        print('invoking ????? ')




c = InvokeCallbackClass()

print(callable(c)) # True

c() # Invoking


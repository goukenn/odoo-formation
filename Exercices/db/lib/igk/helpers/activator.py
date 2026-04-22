class Activator:
    @staticmethod
    def CreateNewInstance(type, dic):
        _t = type()
        for k, v in dic.items():
            _t.__setattr__(k,v)
        return _t
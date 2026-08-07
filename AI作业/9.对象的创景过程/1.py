# 实现类的单例模式

class Singleton:
    _instance = None
    def __new__(cls, *args, **kwags):
        print(args)
        print(kwags)
        if cls._instance == None:
            super().__new__(cls)
        else:
            return cls._instance
    def __init__(self):
        pass
i1 = Singleton(1, name = 1)
i2 = Singleton(2, name = 2)
print(i1 == i2)

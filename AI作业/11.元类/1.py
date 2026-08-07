"""
编写一个元类 SingletonMeta，使得任何使用该元类的类都自动成为单例模式：
"""
class SingletonMeta(type):
    _instance = {}
    # 控制实例的产生
    def __call__(cls, *args, **kwargs):
        if cls.__name__ not in SingletonMeta._instance:
            SingletonMeta._instance[cls.__name__] = super().__call__(*args, **kwargs)
        return SingletonMeta._instance[cls.__name__]
 
class Database(metaclass=SingletonMeta):
    def __init__(self, host):
        self.host = host
 
db1 = Database("localhost") # SingletonMeta.__call__(Database, "localhost")
db2 = Database("remote") # SingletonMeta.__call__(Database, "remote")



print(db1 is db2)  # 应该输出 True
print(db1.host)    # 应该输出 localhost
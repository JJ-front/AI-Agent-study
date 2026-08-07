"""
编写一个元类 LogMeta，自动为类中每个非私有方法（即不以 _ 开头的方法）添加执行日志。调用方法时，先打印 [LOG] 调用 {方法名}，再执行原方法：
"""
class LogMeta(type):
    @staticmethod
    def Log_func(func):
        def new_func(*args, **kwargs):
            print(f"[LOG] 调用 {func.__name__}")
            return func(*args, **kwargs)
        return new_func
    def __new__(mcs, name, bases, namespace):
        for key, value in namespace.items():
            if not key.startswith('_') and callable(value):
                namespace[key] = LogMeta.Log_func(value)
        return super().__new__(mcs, name, bases, namespace)
 
class Calculator(metaclass=LogMeta):
    def add(self, a, b):
        return a + b
    
    def sub(self, a, b):
        return a - b
 
calc = Calculator()
print(calc.add(3, 5))
print(calc.sub(10, 4))
 
# 应该输出：
# [LOG] 调用 add
# 8
# [LOG] 调用 sub
# 6
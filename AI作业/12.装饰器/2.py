# 实现wraps装饰器，用于不改变函数的名称和注释
 
 
def wraps(func):
    def new_func(warpper):
        warpper.__name__ = func.__name__
        warpper.__doc__ = func.__doc__
        return warpper
    return new_func
 
def my_decorator(func):
    @wraps(func)
    def wrapper():
        print("函数执行前")
        func()
        print("函数执行后")
 
    return wrapper
 
 
@my_decorator
def say_hello():
    """打招呼"""
    print("Hello!")
 
 
say_hello()
# 输出：
# 函数执行前
# Hello!
# 函数执行后
print("name", say_hello.__name__)
print("doc", say_hello.__doc__)
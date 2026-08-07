def repeat(n):
    def repeat_docrator(func):
        def func_warpper(*args):
            i = 0
            while n != i:
                func(*args)
                i += 1 
        return func_warpper
    return repeat_docrator
 
 
@repeat(3)
def say_hello(s):
    print(s)
 
 
say_hello(1)  # 输出: 1 1 1
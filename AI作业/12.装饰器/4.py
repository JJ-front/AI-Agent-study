# 编写一个装饰器 cache，缓存函数的计算结果。当使用相同的参数调用函数时，直接返回缓存的结果：

def cache(func):
    params_dict = {}
    def func_warpper(n):
        if n not in params_dict:
            params_dict[n] = func(n)
        return params_dict[n] 
    return func_warpper
 
@cache
def fibonacci(n):
    if n < 3:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(50))  # 应该快速返回结果

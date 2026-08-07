import time
 
def timer(func):
    def new_func():
        start = time.time()
        func()
        use_time = time.time() - start
        print(f"{func.__name__} 执行时间：{use_time}")
    return new_func
 
@timer
def slow_function():
    time.sleep(1)
    return "Done"
 
slow_function()
# 输出：slow_function 执行时间: 1.0012 秒
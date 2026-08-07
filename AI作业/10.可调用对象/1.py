"""
编写一个 Counter 类：

初始化时指定起始值
每次调用实例，计数器值加 1
支持 reset() 方法重置为初始值
支持 get() 方法获取当前值
"""

class Counter:
    count = 0


    def __init__(self, init_value):
        Counter.count = init_value
        self.init_value = init_value
    def __call__(self):
        Counter.count += 1
        return Counter.count
    def reset(self):
        Counter.count = self.init_value
    def get(self):
        return Counter.count

c = Counter(10)
print(c())      # 11
c()             
print(c.get())  # 12
c.reset()
print(c.get())  # 10
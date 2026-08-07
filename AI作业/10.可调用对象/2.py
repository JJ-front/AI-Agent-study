# 下面代码的输出是什么
class A:
    def __call__(self):
        print("A called")
 
class B(A):
    def __call__(self):
        print("B called")
        super().__call__()
 
b = B()
b()

# 输出结果
# B called
# A called
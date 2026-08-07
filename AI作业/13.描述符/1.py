class Descriptor:
    def __get__(self, instance, owner):
        print(f"__get__ called, instance={instance}, owner={owner}")
        return 42
 
    def __set__(self, instance, value):
        print(f"__set__ called, instance={instance}, value={value}")
 
 
class A:
    x = Descriptor()
 
 
a = A()
print(a.x) # __get__ called, instance={instance}, owner={owner} 42
a.x = 100 # __set__ called, instance={instance}, value={value}
a.__dict__["x"] = "instance"
print(a.x) # __get__ called, instance=<__main__.A object at 0x000001DE101E3FA0>, owner=<class '__main__.A'> 42
print(a.__dict__) # { "x": "instance" }
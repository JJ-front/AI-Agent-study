
import asyncio
 
loop = asyncio.new_event_loop()
 
 
def delayed():
    print(1)
    loop.call_later(0, lambda: print(2))
    loop.call_soon(lambda: print(3))
 
 
def soon():
    print(4)
    loop.call_soon(lambda: print(5))
 
 
loop.call_later(0, delayed)
loop.call_soon(soon)
 
 
loop.run_forever()
print("done")

# 打印结果
# 4
# 1
# 5 
# 3
# 2
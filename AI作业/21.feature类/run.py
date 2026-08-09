import asyncio

# 将传入的函数放入到时间循环中
def run(func):
    loop = asyncio.new_event_loop() # 创建事件循环
    asyncio.set_event_loop(loop) # 绑定事件循环到当前线程
    loop.call_soon(func) # 将传入函数加入到ready队列
    loop.run_forever() # 开启事件循环

import asyncio
from gather import gather


# 延时函数
def async_delay(duration: int):
    # 拿到当前事件循环对象
    loop = asyncio.get_running_loop()
    # 创建feature实例
    future = loop.create_future()
    # duration秒后执行feature的set_result函数，作用是标记feature状态为已完成
    loop.call_later(duration, future.set_result, None)
    return future


class Event:
    def __init__(self) -> None:
        self.future: None | asyncio.Future = None

    async def wait(self):
        self.future = asyncio.Future()
        await self.future

    def set(self):
        if self.future:
            self.future.set_result(None)


async def test():
    event = Event()

    async def waiter():
        print("waiter: 开始等待")
        await event.wait()
        print("waiter: 被唤醒")

    async def setter():
        print("setter: 1秒后设置事件")
        await async_delay(1)
        event.set()
        print("setter: 事件已设置")

    await gather(waiter(), setter())


asyncio.run(test())

# 预期结果：
""" 
waiter: 开始等待
setter: 1秒后设置事件
setter: 事件已设置
waiter: 被唤醒 
"""

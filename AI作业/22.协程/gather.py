import asyncio
from typing import Coroutine


# 延时函数
def async_delay(duration: int):
    # 拿到当前事件循环对象
    loop = asyncio.get_event_loop()
    # 创建feature实例
    future = loop.create_future()
    # duration秒后执行feature的set_result函数，作用是标记feature状态为已完成
    loop.call_later(duration, future.set_result, None)
    return future


def gather(*args: Coroutine) -> asyncio.Future:
    future = asyncio.Future()
    # 存放feature的完成结果
    result = [None] * len(args)
    finished_count = 0  # 完成数量

    def callback(r, i):
        nonlocal finished_count
        result[i] = r.result()
        finished_count += 1
        if finished_count == len(args):
            future.set_result(result)

    for i, item in enumerate(args):
        asyncio.create_task(item).add_done_callback(
            lambda fu, index=i: callback(fu, index)
        )

    return future


async def coro(name: str, duration: int):
    await async_delay(duration)
    return f"{name} 完成"


async def main():
    results = await gather(
        coro("A", 2),
        coro("B", 1),
        coro("C", 3),
    )
    print(results)  # 预期: ['A 完成', 'B 完成', 'C 完成']


# asyncio.run(main())

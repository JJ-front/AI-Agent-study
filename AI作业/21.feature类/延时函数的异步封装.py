import asyncio
import run

# 延时函数
def async_delay(duration: int):
    # 拿到当前事件循环对象
    loop = asyncio.get_event_loop()
    # 创建feature实例
    future = loop.create_future()
    # duration秒后执行feature的set_result函数，作用是标记feature状态为已完成
    loop.call_later(duration, future.set_result, None)
    return future


def main():
    # 2秒后feature完成，然后执行add_done_callback回调打印 2 seconds have passed
    async_delay(2).add_done_callback(lambda _: print("2 seconds have passed"))
    print("不影响其他代码的执行")

# 放入事件循环执行
run.run(main)

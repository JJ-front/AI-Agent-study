import socket
import asyncio
import run
import sys

# Windows兼容性修复
if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# 异步创建网络连接通道
def async_connect(host: str, port: int) -> asyncio.Future:
    loop = asyncio.get_running_loop()  # 获取当前的事件循环
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建一个socket
    sock.setblocking(False)  # 设置为非阻塞模式
    try:
        sock.connect((host, port)) # 这里会报错，因为连接不能阻塞，因此进入except 但是连接还在继续创建
    except BlockingIOError:
        pass

    fut = asyncio.Future() # 创建feature对象

    def on_writable() -> None:
        # 看一下socked是否报错
        # 当有数据可写，但是还未进入缓冲区时候，会报错
        err = sock.getsockopt(socket.SOL_SOCKET, socket.SO_ERROR)
        # 直接移除可写事件，本函数的目的只是为了建立连接，当on_writable执行，意味着连接建立结束 因此就不需要监听这个事件了 后续依赖feature
        loop.remove_writer(sock)
        if err == 0:
            fut.set_result(sock) # 没有错误直接将feature抛出去
        else:
            fut.set_exception(ConnectionError(f"Connect failed: {err}"))

    # 监听文件描述符的可写事件，当socket连接成功时，文件描述符会变为可写
    loop.add_writer(sock, on_writable)
    return fut

# 异步读取响应结果
def async_read(sock: socket.socket, host: str, port: int, path: str) -> asyncio.Future:
    loop = asyncio.get_running_loop() # 拿到事件循环对象
    fut = asyncio.Future() # 创建feature
    # 请求原始报文
    req = f"""GET {path} HTTP/1.1
Host: {host}:{port}
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en-GB;q=0.8,en;q=0.7,ru;q=0.6
Cache-Control: no-cache
Connection: close
Pragma: no-cache
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36

""".replace("\n", "\r\n")
    sock.setblocking(False) # 不要阻塞
    sock.send(req.encode()) # 编码后发送
    data = b""

    def on_readable() -> None:
        nonlocal data
        try:
            chunk = sock.recv(4096) # 一次最大接受2M
            if chunk:
                data += chunk
            else:
                loop.remove_reader(sock) # 读完了就移除
                fut.set_result(data.decode()) # 然后把结果抛出去
        except BlockingIOError:
            pass

    loop.add_reader(sock, on_readable) # 当响应回来后sock变为可读，执行on_readable
    return fut

# 异步请求
def async_request(host: str, port: int, path: str) -> asyncio.Future:
    fut = asyncio.Future() 

    def on_connected(f: asyncio.Future) -> None:
        try:
            sock = f.result() # 拿到sock对象
            read_fut = async_read(sock, host, port, path) # 获取响应feature
            read_fut.add_done_callback(lambda rf: fut.set_result(rf.result())) #抛出响应结果
        except Exception as e:
            fut.set_exception(e)

    connect_fut = async_connect(host, port)
    connect_fut.add_done_callback(on_connected)
    return fut


def main() -> None:
    def on_response(f: asyncio.Future) -> None:
        try:
            response = f.result() # 拿到相应结果
            print(response)
        except Exception as e:
            print(f"Request failed: {e}")
        finally:
            asyncio.get_running_loop().stop()

    async_request("shae-learn.yuanjin.tech", 80, "/").add_done_callback(on_response)

# 放入事件循环执行
run.run(main)

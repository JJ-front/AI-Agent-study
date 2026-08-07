import sys
import os
import json
from typing import Generator
import requests
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()
_API_BASE: str = os.getenv("API_BASE", "https://api.openai.com/v1")
_MODEL_NAME: str = os.getenv("MODEL_NAME", "gpt-3.5-turbo")
_API_KEY: str = os.getenv("API_KEY", "")
# 拼接口路径
_URL: str = f"{_API_BASE.rstrip('/')}/chat/completions"

if not _API_KEY:
    print("错误: 请在 .env 文件中配置 API_KEY")
    sys.exit(1)


def completions(messages: list[dict[str, str]]) -> Generator[str, None, None]:
    headers: dict[str, str] = {
        "Authorization": f"Bearer {_API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": _MODEL_NAME,
        "messages": messages,
        "stream": True,
    }
    # 开启流式传输
    resp = requests.post(_URL, headers=headers, json=payload, stream=True)
    resp.raise_for_status() # 检查是否有错误响应码 有就报错 SSE协议

    for line in resp.iter_lines():
        if not line:
            continue
        text: str = line.decode("utf-8") # utf-8解码
        if not text.startswith("data: "):
            continue
        data_str = text[6:] # SSE相应是data: 开头，所以取后面的才是数据
        if data_str.strip() == "[DONE]": # 空响应不要
            break
        try:
            chunk = json.loads(data_str) # 字符串json化
            delta = chunk["choices"][0].get("delta", {})
            content = delta.get("content", "")
            if content:
                yield content
        except (json.JSONDecodeError, KeyError, IndexError):
            continue

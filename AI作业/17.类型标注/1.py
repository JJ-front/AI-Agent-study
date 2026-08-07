# 下面代码的类型标注是否正确？如果不正确，如何修改？
from typing import List, Dict 
 
 
def process_data(items: List) -> Dict:
    """处理数据项"""
    result = {}
    for item in items:
        result[item["id"]] = item["value"]
    return result
 
 
def find_max(a: int, b: int) -> int | None:
    """返回较大的数"""
    if a == b:
        return None
    return a if a > b else b

# 结论：修复联合类型为Optional[int]
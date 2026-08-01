"""
实现函数 `merge_dicts`，接收不定数量的字典参数，将它们合并为一个大字典。

合并规则：求并集，如果有相同的键，后传入的字典中的值覆盖先传入的字典中的值（浅合并即可）
"""

def merge_dicts(*args):
    new_dict = {}
    for item in args:
       new_dict.update(item)
    return new_dict

d1 = {"a": 1, "b": [1, 2]}
d2 = {"b": [3], "c": "hello"}
d3 = {"a": 10, "d": True}

merged = merge_dicts(d1, d2, d3)
print(merged)
# # {'a': 10, 'b': [3], 'c': 'hello', 'd': True}

print(merge_dicts(d1))
# {'a': 1, 'b': [1, 2]}

print(merge_dicts())
# {}
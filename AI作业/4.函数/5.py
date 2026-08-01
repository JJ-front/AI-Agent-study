"""
实现函数 `to_linked_list`，接收一个列表或元组，将其转换为一个链表结构并返回。
"""


def to_linked_list(list_tuple):
    if len(list_tuple) == 0:
        return None
    head = {"value": list_tuple[0], "next": {}}
    current = head
    for i, item in enumerate(list_tuple):
        if i == 0:
            pass
        else:
            current['next']['vaule'] = list_tuple[i]
            current['next']['next'] = {}
            current = current['next']
    return  head

linked1 = to_linked_list((1, 2, 3))
print(linked1)
# {'value': 1, 'next': {'value': 2, 'next': {'value': 3, 'next': None}}}

linked2 = to_linked_list([10, 20])
print(linked2)
# {'value': 10, 'next': {'value': 20, 'next': None}}

print(to_linked_list([]))  # None
    


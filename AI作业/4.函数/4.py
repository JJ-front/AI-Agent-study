"""
实现函数 `flatten`，接收一个可能包含嵌套列表的列表（如 `[1, [2, 3], [[4], 5]]`），返回一个将所有元素展开后的一维列表（如 `[1, 2, 3, 4, 5]`）。
"""
# def flatten(multidimensional_list): 
#     flat_list = []
#     for item in multidimensional_list:
#         if (type(item) == list):
#             flat_list.extend(flatten(item))
#         else: 
#             flat_list.append(item)
#     return flat_list

# nested1 = [1, [2, 3], [[4], 5]]
# print(flatten(nested1))  # [1, 2, 3, 4, 5]

# nested2 = [[[1]], 2, [3, [4, [5]]]]
# print(flatten(nested2))  # [1, 2, 3, 4, 5]

# print(flatten([]))       # []
# print(flatten([1, 2, 3]))  # [1, 2, 3]

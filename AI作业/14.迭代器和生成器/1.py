# 编写一个生成器函数 flatten，将嵌套的列表扁平化：
def flatten(nested_list):
    for i in nested_list:
        if isinstance(i, list):
            yield from flatten(i)
        else:
            yield i
 
 
nested = [1, [2, [3, 4], 5], 6, [7, 8]]
print(list(flatten(nested)))
# [1, 2, 3, 4, 5, 6, 7, 8]
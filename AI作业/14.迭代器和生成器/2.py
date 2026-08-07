import math
# 编写一个生成器，模拟从数据库分页读取数据：
def paginated_query(total_items, page_size):
    """
    模拟分页查询
    total_items: 总数据量
    page_size: 每页大小
    每次 yield 返回一页数据（列表）
    """
    page_num = math.ceil(total_items / page_size)
    for i in range(page_num):
        start = page_size * i
        end = total_items if page_size * (i + 1) > total_items else page_size * (i + 1)
        yield [i for i in range(start, end)]
 
 
for page in paginated_query(25, 10):
    print(page)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
# [20, 21, 22, 23, 24]

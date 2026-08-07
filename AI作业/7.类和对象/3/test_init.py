from zuoye import LinkedList

def test_init_with_list():
    ll = LinkedList([1, 2, 3, 4, 5])
    print("测试用列表初始化:")
    print(f"  是否为空: {ll.is_empty()}")  # 预期: False
    print(f"  长度: {ll.get_length()}")    # 预期: 5
    print(f"  字符串: '{ll.__str__()}'")             # 预期: '1 -> 2 -> 3 -> 4 -> 5'
    print(f"  转列表: {ll.to_list()}")     # 预期: [1, 2, 3, 4, 5]

def test_init_with_tuple():
    ll = LinkedList((10, 20, 30))
    print("测试用元组初始化:")
    print(f"  字符串: '{ll.__str__()}'")             # 预期: '10 -> 20 -> 30'
    print(f"  转列表: {ll.to_list()}")     # 预期: [10, 20, 30]

def test_init_with_set():
    ll = LinkedList({1, 2, 3})
    print("测试用集合初始化:")
    print(f"  长度: {ll.get_length()}")    # 预期: 3
    print(f"  转列表(排序后): {sorted(ll.to_list())}")  # 预期: [1, 2, 3]

test_init_with_list()
test_init_with_tuple()
test_init_with_set()

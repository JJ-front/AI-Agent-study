from zuoye import LinkedList
# 第6块：find 和 get 测试

# ==================== 测试 find ====================
def test_find_existing():
    ll = LinkedList([10, 20, 30, 20, 40])
    print("测试 find (存在):")
    index = ll.find(20)
    print(f"  查找20: {index}")               # 预期: 1 (第一个匹配)
    print()

def test_find_not_existing():
    ll = LinkedList([10, 20, 30])
    print("测试 find (不存在):")
    index = ll.find(40)
    print(f"  查找40: {index}")               # 预期: -1
    print()

def test_find_empty():
    ll = LinkedList()
    print("测试 find (空链表):")
    index = ll.find(10)
    print(f"  查找10: {index}")               # 预期: -1
    print()

# ==================== 测试 get ====================
def test_get_existing():
    ll = LinkedList([10, 20, 30, 40])
    print("测试 get (存在):")
    value = ll.get(2)
    print(f"  获取索引2: {value}")            # 预期: 30
    print()

def test_get_head():
    ll = LinkedList([10, 20, 30])
    print("测试 get (头节点):")
    value = ll.get(0)
    print(f"  获取索引0: {value}")            # 预期: 10
    print()

def test_get_tail():
    ll = LinkedList([10, 20, 30])
    print("测试 get (尾节点):")
    value = ll.get(2)
    print(f"  获取索引2: {value}")            # 预期: 30
    print()

def test_get_out_of_range():
    ll = LinkedList([10, 20, 30])
    print("测试 get (索引越界):")
    value = ll.get(5)
    print(f"  获取索引5: {value}")            # 预期: None
    print()

def test_get_negative():
    ll = LinkedList([10, 20, 30])
    print("测试 get (负索引):")
    value = ll.get(-1)
    print(f"  获取索引-1: {value}")           # 预期: None
    print()

def test_get_empty():
    ll = LinkedList()
    print("测试 get (空链表):")
    value = ll.get(0)
    print(f"  获取索引0: {value}")            # 预期: None
    print()

test_find_existing()
test_find_not_existing()
test_find_empty()
test_get_existing()
test_get_head()
test_get_tail()
test_get_out_of_range()
test_get_negative()
test_get_empty()
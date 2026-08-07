from zuoye import LinkedList

# ==================== 测试 traverse ====================
def test_traverse():
    ll = LinkedList([1, 2, 3, 4])
    print("测试 traverse:")
    result = []
    def callback(index, value):
        result.append(f"索引{index}={value}")
    ll.traverse(callback)
    print(f"  遍历结果: {', '.join(result)}")  # 预期: 索引0=1, 索引1=2, 索引2=3, 索引3=4
    print()

def test_traverse_empty():
    ll = LinkedList()
    print("测试 traverse (空链表):")
    result = []
    def callback(index, value):
        result.append(f"索引{index}={value}")
    ll.traverse(callback)
    print(f"  遍历结果: {result}")             # 预期: []
    print()

# ==================== 测试 to_list ====================
def test_to_list():
    ll = LinkedList([1, 2, 3])
    print("测试 to_list:")
    lst = ll.to_list()
    print(f"  转列表: {lst}")                 # 预期: [1, 2, 3]
    # 测试是否返回新列表
    lst.append(4)
    print(f"  原链表不变: {ll.to_list()}")    # 预期: [1, 2, 3]
    print()

# ==================== 测试 __str__ ====================
def test_str():
    ll1 = LinkedList([1, 2, 3])
    print("测试 __str__:")
    print(f"  [1,2,3] -> '{ll1.__str__()}'")            # 预期: '1 -> 2 -> 3'
    
    ll2 = LinkedList([1])
    print(f"  [1] -> '{ll2.__str__()}'")                # 预期: '1'
    
    ll3 = LinkedList()
    print(f"  [] -> '{ll3.__str__()}'")                 # 预期: ''
    print()

test_traverse()
test_traverse_empty()
test_to_list()
test_str()
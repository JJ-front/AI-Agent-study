from zuoye import LinkedList
# 第4块：delete_by_value 测试

# ==================== 测试 delete_by_value ====================
def test_delete_by_value_existing():
    ll = LinkedList([1, 2, 3, 2, 4])
    print("测试 delete_by_value (存在):")
    result = ll.delete_by_value(2)
    print(f"  删除第一个2: {result}")         # 预期: True
    print(f"  删除后: {ll.to_list()}")        # 预期: [1, 3, 2, 4]
    print()

def test_delete_by_value_head():
    ll = LinkedList([1, 2, 3])
    print("测试 delete_by_value (删除头节点):")
    result = ll.delete_by_value(1)
    print(f"  删除1: {result}")               # 预期: True
    print(f"  删除后: {ll.to_list()}")        # 预期: [2, 3]
    print()

def test_delete_by_value_not_existing():
    ll = LinkedList([1, 2, 3])
    print("测试 delete_by_value (不存在):")
    result = ll.delete_by_value(4)
    print(f"  删除4: {result}")               # 预期: False
    print(f"  链表保持不变: {ll.to_list()}")  # 预期: [1, 2, 3]
    print()

def test_delete_by_value_empty():
    ll = LinkedList()
    print("测试 delete_by_value (空链表):")
    result = ll.delete_by_value(1)
    print(f"  删除1: {result}")               # 预期: False
    print()

test_delete_by_value_existing()
test_delete_by_value_head()
test_delete_by_value_not_existing()
test_delete_by_value_empty()

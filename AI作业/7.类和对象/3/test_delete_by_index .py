from zuoye import LinkedList

# 第5块：delete_by_index 测试

# ==================== 测试 delete_by_index ====================
def test_delete_by_index_middle():
    ll = LinkedList([1, 2, 3, 4, 5])
    print("测试 delete_by_index (删除中间):")
    deleted = ll.delete_by_index(2)
    print(f"  删除索引2: {deleted}")          # 预期: True
    print(f"  删除后: {ll.to_list()}")        # 预期: [1, 2, 4, 5]
    print()

def test_delete_by_index_head():
    ll = LinkedList([1, 2, 3])
    print("测试 delete_by_index (删除头节点):")
    deleted = ll.delete_by_index(0)
    print(f"  删除索引0: {deleted}")          # 预期: True
    print(f"  删除后: {ll.to_list()}")        # 预期: [2, 3]
    print()

def test_delete_by_index_tail():
    ll = LinkedList([1, 2, 3])
    print("测试 delete_by_index (删除尾节点):")
    deleted = ll.delete_by_index(2)
    print(f"  删除索引2: {deleted}")          # 预期: True
    print(f"  删除后: {ll.to_list()}")        # 预期: [1, 2]
    print()

def test_delete_by_index_out_of_range():
    ll = LinkedList([1, 2, 3])
    print("测试 delete_by_index (索引越界):")
    deleted = ll.delete_by_index(5)
    print(f"  删除索引5: {deleted}")          # 预期: False
    print(f"  链表保持不变: {ll.to_list()}")  # 预期: [1, 2, 3]
    print()

def test_delete_by_index_negative():
    ll = LinkedList([1, 2, 3])
    print("测试 delete_by_index (负索引):")
    deleted = ll.delete_by_index(-1)
    print(f"  删除索引-1: {deleted}")         # 预期: False
    print(f"  链表保持不变: {ll.to_list()}")  # 预期: [1, 2, 3]
    print()

def test_delete_by_index_empty():
    ll = LinkedList()
    print("测试 delete_by_index (空链表):")
    deleted = ll.delete_by_index(0)
    print(f"  删除索引0: {deleted}")          # 预期: False
    print()

test_delete_by_index_middle()
test_delete_by_index_head()
test_delete_by_index_tail()
test_delete_by_index_out_of_range()
test_delete_by_index_negative()
test_delete_by_index_empty()
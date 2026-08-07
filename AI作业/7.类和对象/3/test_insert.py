from zuoye import LinkedList

# 第3块：insert 测试

# ==================== 测试 insert ====================
def test_insert_beginning():
    ll = LinkedList([2, 3, 4])
    print("测试 insert 到开头:")
    ll.insert(0, 1)
    print(f"  在索引0插入1: {ll.to_list()}")  # 预期: [1, 2, 3, 4]
    print()

def test_insert_middle():
    ll = LinkedList([1, 2, 4, 5])
    print("测试 insert 到中间:")
    ll.insert(2, 3)
    print(f"  在索引2插入3: {ll.to_list()}")  # 预期: [1, 2, 3, 4, 5]
    print()

def test_insert_end():
    ll = LinkedList([1, 2, 3])
    print("测试 insert 到末尾:")
    ll.insert(3, 4)
    print(f"  在索引3插入4: {ll.to_list()}")  # 预期: [1, 2, 3, 4]
    print()

def test_insert_out_of_range():
    ll = LinkedList([1, 2, 3])
    print("测试 insert 索引越界:")
    ll.insert(5, 4)
    print(f"  在索引5插入4: {ll.to_list()}")  # 根据你的实现调整预期
    print()

test_insert_beginning()
test_insert_middle()
test_insert_end()
test_insert_out_of_range()
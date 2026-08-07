from zuoye import LinkedList

# 第2块：append 和 prepend 测试

# ==================== 测试 append ====================
def test_append():
    ll = LinkedList()
    print("测试 append:")
    ll.append(1)
    ll.append(2)
    ll.append(3)
    print(f"  追加1,2,3后: {ll.to_list()}")  # 预期: [1, 2, 3]
    print(f"  长度: {ll.get_length()}")      # 预期: 3
    print()

# ==================== 测试 prepend ====================
def test_prepend():
    ll = LinkedList()
    print("测试 prepend:")
    ll.prepend(1)
    ll.prepend(2)
    ll.prepend(3)
    print(f"  插入3,2,1后: {ll.to_list()}")  # 预期: [3, 2, 1]
    print(f"  长度: {ll.get_length()}")      # 预期: 3
    print()
test_append()
test_prepend()
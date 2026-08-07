from zuoye import LinkedList
def test_mixed_operations():
    print("=" * 50)
    print("测试混合操作:")
    ll = LinkedList([1, 2, 3])
    print(f"  初始: {ll.to_list()}")
    
    ll.append(4)
    print(f"  追加4: {ll.to_list()}")         # 预期: [1, 2, 3, 4]
    
    ll.prepend(0)
    print(f"  开头加0: {ll.to_list()}")       # 预期: [0, 1, 2, 3, 4]
    
    ll.insert(3, 99)
    print(f"  索引3插入99: {ll.to_list()}")   # 预期: [0, 1, 2, 99, 3, 4]
    
    ll.delete_by_value(99)
    print(f"  删除99: {ll.to_list()}")        # 预期: [0, 1, 2, 3, 4]
    
    ll.delete_by_index(0)
    print(f"  删除索引0: {ll.to_list()}")     # 预期: [1, 2, 3, 4]
    
    print(f"  查找3的索引: {ll.find(3)}")     # 预期: 2
    print(f"  获取索引2的值: {ll.get(2)}")    # 预期: 3
    print(f"  链表长度: {ll.get_length()}")   # 预期: 4
    print(f"  是否为空: {ll.is_empty()}")     # 预期: False
    print()
test_mixed_operations()
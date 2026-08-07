"""
请实现一个单链表类 LinkedList，支持以下操作：

需要实现的方法：

方法	说明
__init__(data=None)	初始化空链表；data 可以是列表、元组或集合，其中的值会被初始化为链表的节点
traverse(callback)	遍历链表，对每个节点值调用 callback(index, value)
__str__()	返回链表的字符串表示，如 "1 -> 2 -> 3"
to_list()	将链表转换为 Python 列表并返回
append(value)	在链表尾部添加一个新节点
prepend(value)	在链表头部添加一个新节点
insert(index, value)	在指定索引位置插入新节点，索引从 0 开始
delete_by_value(value)	删除第一个值等于 value 的节点，返回是否删除成功
delete_by_index(index)	删除指定索引位置的节点，返回被删除的值，索引越界时返回 None
find(value)	查找值等于 value 的节点，返回其索引，不存在返回 -1
get(index)	获取指定索引位置的值，索引越界时返回 None
get_length()	返回链表长度
is_empty()	判断链表是否为空

提示： 你可能需要先定义一个 Node 类来表示链表节点。
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, data = []):
        data = list(data)
        if data == Node or len(data) == 0:
            self.head = None
            return None
        head = Node(data[0])
        current = head
        for item in data[1:]:
            next_node = Node(item)
            current.next = next_node
            current = next_node
        self.head = head
    def traverse(self, callback):
        if self.is_empty():
            return
        i = 0
        callback(i, self.head.value)
        current = self.head.next
        while current != None:
            i += 1
            callback(i, current.value)
            current = current.next
    def __str__(self):
        if self.is_empty():
            return ''
        new_str = ''
        new_str += str(self.head.value) + "->"
        current = self.head.next
        while current != None:
            new_str += str(current.value) + '->'
            current = current.next
        return new_str[:-2]
    def to_list(self):
        if self.is_empty():
            return
        new_list = []
        new_list.append(self.head.value)
        current = self.head.next
        while current != None:
            new_list.append(current.value)
            current = current.next
        return new_list
    def append(self, value):
        if self.is_empty():
            self.head = Node(value)
            return
        next = Node(value)
        current = self.head
        while current.next != None:
            current = current.next
        current.next = next
    def prepend(self, value):
        if self.is_empty():
           self.head = Node(value)
           return
        head = Node(value)
        head.next = self.head
        self.head = head
    def insert(self, index, value):
        node = Node(value)
        if index == 0:
           self.prepend(value)
        else:
            i = 0
            current = self.head
            pre = self.head
            while current != None and i != index:
                if i != 0:
                    pre = pre.next
                current = current.next
                i += 1
            if current == None:
                return
            node.next = current
            pre.next = node
    def delete_by_value(self, value):
        if self.is_empty():
            return False
        if value == self.head.value:
            self.head = self.head.next
            return True
        current = self.head
        pre = self.head
        next = self.head
        i = 0
        while current != None and current.value != value:
            if i != 0:
                pre = pre.next
            if current.next == None:
                next = current.next
            else:
                next = current.next.next
            i += 1
            current = current.next
        if current == None:
            return False
        pre.next = next
        return True
    def delete_by_index(self, index):
        if self.is_empty():
            return False
        if index == 0:
            self.head = self.head.next
            return True
        i = 0
        pre = self.head
        next = self.head
        current = self.head
        while i != index and current != None:
            if i != 0:
                pre = pre.next
            if current.next == None:
                next = current.next
            else:
                next = current.next.next
            current = current.next
            i += 1
        if current == None:
            return False
        pre.next = next
        return True
    def find(self, value):
        if self.is_empty():
            return -1
        current = self.head
        i = 0
        if current.value == value:
            return i
        while current != None and current.value != value:
            current = current.next
            i += 1
        if current == None:
            return -1
        return i
    def get(self, index):
        if self.is_empty():
            return
        current = self.head
        i = 0
        while i != index and current != None:
            current = current.next
            i += 1
        if current == None:
            return None
        return current.value
    def get_length(self):
        if self.is_empty():
            return
        current = self.head
        i = 0
        while current != None:
            current = current.next
            i += 1
        return i
    def is_empty(self):
        return self.head == None


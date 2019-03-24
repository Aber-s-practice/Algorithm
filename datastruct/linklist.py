import weakref


class Node:
    """
    链表节点
    """

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next: Node = next_node

    def __str__(self):
        return f"[{self.data}]"


class NormalLinkList:
    """
    不带头节点的链表
    """

    def __init__(self):
        self.node: Node = None
        self.length = 0

    def __str__(self):
        point = self.node
        s = f"NormalLinkList: {point}"
        if point is not None:
            while point.next is not None:
                point = point.next
                s += f" -> {point}"
        return s

    def insert(self, node: Node, index: int):
        if index > self.length:
            raise IndexError("超出了链表长度")
        if index == 0:
            node.next = self.node
            self.node = node
        else:
            point = self.node
            for _ in range(index-1):
                point = point.next
            point.next = node
        self.length += 1

    def remove(self, index: int):
        if index > self.length - 1:
            raise IndexError("超出了链表长度")
        if index == 0:
            self.node = self.node.next
        else:
            point = self.node
            for _ in range(index-1):
                point = point.next
            point.next = point.next.next
        self.length -= 1


class HeadLinkList:
    """
    带头节点的链表
    """

    def __init__(self):
        self.head: Node = Node()
        self.length = 0

    def __str__(self):
        point = self.head
        s = "HeadLinkList: [head]"
        while point.next is not None:
            point = point.next
            s += f" -> {point}"
        return s

    def insert(self, node: Node, index: int):
        if index > self.length:
            raise IndexError("超出了链表长度")
        point = self.head
        for _ in range(index):
            point = point.next
        node.next = point.next
        point.next = node
        self.length += 1

    def remove(self, index: int):
        if index > self.length - 1:
            raise IndexError("超出了链表长度")
        point = self.head
        for _ in range(index):
            point = point.next
        point.next = point.next.next
        self.length -= 1


class DoublyNode:
    """
    双向链表节点
    """

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next: DoublyNode = next_node
        self.__pre = None

    @property
    def pre(self):
        return self.__pre

    @pre.setter
    def pre(self, node):
        self.__pre = weakref.ref(node)

    @pre.getter
    def pre(self):
        return self.__pre()

    def __str__(self):
        return f"[{self.data}]"


class DoublyLinkedList:
    """
    双向链表
    """

    def __init__(self):
        self.head = DoublyNode()
        self.tail = DoublyNode()
        self.head.next = self.tail
        self.tail.pre = self.head
        self.length = 0

    def __str__(self):
        point = self.head
        s = "DoublyLinkList: [head]"
        for _ in range(self.length):
            point = point.next
            s += f" <-> {point}"
        s += " <-> [tail]"
        return s

    def insert(self, node: DoublyNode, index: int):
        if index > self.length:
            raise IndexError("超出了链表长度")
        if index >= self.length // 2:
            point = self.tail
            for _ in range(self.length-index+1):
                point = point.pre
        else:
            point = self.head
            for _ in range(index):
                point = point.next
        node.next = point.next
        point.next = node
        node.pre = point
        if node.next is not None:
            node.next.pre = node
        self.length += 1

    def remove(self, index: int):
        if index > self.length - 1:
            raise IndexError("超出了链表长度")
        if index >= self.length // 2:
            point = self.tail
            for _ in range(self.length-index+1):
                point = point.pre
        else:
            point = self.head
            for _ in range(index):
                point = point.next
        point.next = point.next.next
        point.next.pre = point
        self.length -= 1

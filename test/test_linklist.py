from datastruct.linklist import *


def test_linklist(l):
    for i in range(5):
        l.insert(Node(i), 0)
    print(l)
    l.remove(2)
    print(l)


l = NormalLinkList()
test_linklist(l)

l = HeadLinkList()
test_linklist(l)


def test_doubly_linklist(l):
    for i in range(5):
        l.insert(DoublyNode(i), 0)
    print(l)
    l.remove(4)
    print(l)


l = DoublyLinkedList()
test_doubly_linklist(l)

class Node:

    def __init__(self, data=None):
        self.data = data
        self.next: Node = None

    def __str__(self):
        return f"[{self.data}]"


class Queue:

    def __init__(self):
        self.__head = Node()
        self.__end = self.__head
        self.length = 0

    @property
    def head(self):
        return None if self.__head.next is None else self.__head.next.data

    def append(self, data):
        self.__end.next = Node(data)
        self.__end = self.__end.next
        self.length += 1

    def poll(self):
        if self.length == 0:
            raise IndexError("Queue is empty")
        data = self.__head.next.data
        self.__head = self.__head.next
        self.length -= 1
        return data

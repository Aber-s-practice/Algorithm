class Stack:
    def __init__(self):
        self.__data = []

    @property
    def length(self):
        return len(self.__data)

    @property
    def top(self):
        """
        仅返回栈顶元素而不出栈, 若栈为空则返回None
        """
        return None if self.length == 0 else self.__data[-1]

    def push(self, data):
        self.__data.append(data)

    def pop(self):
        return self.__data.pop()

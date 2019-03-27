from datastruct.stack import Stack

stack = Stack()

for i in range(5):
    stack.push(i)

assert stack.top == 4, f"Stack top is {stack.top}"

for i in range(5):
    stack.pop()

assert stack.top == None, f"Stack top is {stack.top}"

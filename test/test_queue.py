from datastruct.queue import Queue

queue = Queue()

for i in range(5):
    queue.append(i)

assert queue.head == 0, f"Queue head is {queue.head}"

for i in range(5):
    queue.poll()

assert queue.head == None, f"Queue head is {queue.head}"

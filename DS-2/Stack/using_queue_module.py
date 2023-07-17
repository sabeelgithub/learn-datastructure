import queue
stack = queue.LifoQueue()
print(stack)
stack.put(1)
stack.put(2)
stack.put(3)
stack.get()
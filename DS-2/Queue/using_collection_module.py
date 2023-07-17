import collections
queue = collections.deque()
queue.append(5)
queue.append(10)
queue.append(15)
queue.popleft()
queue.clear()
print(queue)
class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None
    def __iter__(self):
        n = self.head
        while n:
            yield n
            n = n.ref

class Queue:
    def __init__(self):
        self.LinkedList = LinkedList()

    def __str__(self):
        if self.LinkedList.head:
            values = [str(n.data) for n in self.LinkedList]
            return '\n'.join(values)
        else:
            return 'Queue is empty'
        
    def isEmpty(self):
        if self.LinkedList.head is None:
            return True
        else:
            return False
    
    def Enqueue(self,data):
        new_node = Node(data)
        if self.LinkedList.head is None:
            self.LinkedList.head = new_node
            return f'item {data} is added at empty linked list'
        else:
            n = self.LinkedList.head
            while n.ref:
                n = n.ref
            n.ref = new_node
            return f'item {data} is added'
        
    def Dequeu(self):
        if self.isEmpty():
            return 'cant delete,beacuse queue is empty'
        else:
          dlt = self.LinkedList.head.data
          self.LinkedList.head = self.LinkedList.head.ref
          return dlt
        
    def peek(self):
        if self.isEmpty():
            return 'we cant get peek,beacuse queue is empty'
        else:
            return self.LinkedList.head.data
    
    def delete(self):
        self.LinkedList.head = None

            
        
queue = Queue()
print(queue.isEmpty())
print(queue.Enqueue(5))
print(queue.Enqueue(10))
print(queue.Enqueue(15))
print('-------')
print(queue.Dequeu())
print('-------')
print(queue.peek())
print('-------')
queue.delete()
print(queue)
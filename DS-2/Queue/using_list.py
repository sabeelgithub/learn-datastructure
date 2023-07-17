class Queue:
    def __init__(self):
        self.list = []
    def __str__(self): 
        if self.list:
            values = self.list.reverse()
            values = [str(i) for i in self.list]
            return '\n'.join(values)
        else:
            return 'queue is empty'
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
    
    def Enqueue(self,value):
        self.list.append(value)
        return f'item {value} is added sussessfully'
    
    def Dequeue(self):
        if self.isEmpty():
            return 'cant delete ,beacuse queue is empty'
        else:
            
            return self.list.pop(0)
    def peek(self):
        if self.isEmpty():
            return 'cant get peek,because queue is empty'
        else:
            return self.list[0]
        
    def delete(self):
        self.list = None


        
queue = Queue()
print(queue.isEmpty())
print(queue.Enqueue(5))
print(queue.Enqueue(10))
print(queue.Enqueue(15))
print(queue.Dequeue())
print('-------')
print(queue.peek())
print('-------')
queue.delete()
print(queue)

        
        
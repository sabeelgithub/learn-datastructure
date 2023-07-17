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


class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()

    def __str__(self):
            if self.LinkedList.head:
                values = [str(x.data) for x in self.LinkedList]
                return '\n'.join(values)
            else :
                return 'its empty'

    def isEmpty(self):
        if self.LinkedList.head is None:
            return True
        else :
            return False
    def push(self,data):
        new_node = Node(data)
        if self.LinkedList.head is None:
            self.LinkedList.head = new_node
            return f'item {data} is added empty linked list'
        else:
            new_node.ref = self.LinkedList.head
            self.LinkedList.head = new_node
            return f'item {data} is added'
        
    def pop(self):
        if self.LinkedList.head is None:
            return 'cant delete beacuse it empty'
        else:
            dlt = self.LinkedList.head.data
            self.LinkedList.head = self.LinkedList.head.ref
            return dlt
    def peek(self):
        if self.LinkedList.head is None:
            return 'cant show peek,its empty'
        else:
            return self.LinkedList.head.data
        
    def delete(self):
        self.LinkedList.head = None
        
stack = Stack()
print(stack.isEmpty())
print(stack.push(5))
print(stack.push(10))
print(stack.push(15))
print('------')
print(stack.pop())
print('------')
print(stack.peek()) 
print('------')
# stack.delete()
print(stack)
              
        
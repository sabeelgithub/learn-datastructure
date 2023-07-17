# --------------- implementation using list -------------#

# implemntation of stack using list without fixed size

class Stack:
    def __init__(self):
        self.list = []

    def __str__(self):
        if self.list:
            value = self.list.reverse()
            value = [str(i) for i in self.list]
            return '\n'.join(value)
        else:
            return 'stack is empty'
        
    
    # is empty
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
    
    # push 
    def push(self,value):
        self.list.append(value)
        print(f'item {value} is added')

    def pop(self):
        if self.isEmpty():
            print('cant delete ,because it already empty')
        else:
            return self.list.pop()
           
    def peek(self):
        if self.isEmpty():
            print('cant return top value,because its empty')
        else:
            return self.list[len(self.list)-1]

    def delete(self):
        self.list = None
    
stack = Stack()
print(stack.isEmpty())
stack.push(5)
stack.push(10)
stack.push(15)
print(stack.isEmpty())
print(stack.pop())

print('--')
print(stack.peek())
print('--')
print(stack)
stack.delete()
print('----')
print(stack)
print('------')

# implemntation of stack using list without fixed size
print('fixed sized stack')
print('-----------')
class FixedStack:
    def __init__(self,fixedSize):
        self.list = []
        self.fixedSize = fixedSize
    
    def __str__(self):
        if self.list:
            values = self.list.reverse()
            values = [str(i) for i in self.list]
            return '\n'.join(values)
        else:
            return 'stack is empty'
        
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
    
    def push(self,value):
        if len(self.list) < self.fixedSize:
            self.list.append(value)
            return f'item {value} added sussefully'
        else:
            return 'cant add, out of size'
    
    def pop(self):
        if self.isEmpty():
            return 'cant delete ,because its empty'
        else:
            return self.list.pop()
        
    def peek(self):
        if self.isEmpty():
            return 'cant see top element,because its empty'
        else:
            return self.list[len(self.list)-1]
        
    def delete(self):
        self.list = None
        
fstack = FixedStack(5)
print(fstack.isEmpty())
print(fstack.push(5))
print(fstack.push(10))
print(fstack.push(15))
print(fstack.push(20))
print(fstack.push(25))
print(fstack.push(30))
print('------')
print(fstack.pop())
print('----')
print(fstack.peek(),'topmost')
print('------')
fstack.delete()
print(fstack)
        
        





    

        
    

        
class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None

class SLL:
    def __init__(self):
        self.head = None
    def forward_traversing(self):
        if self.head is None:
            print('cant frontward traverse,beacuse its empty')
        else:
            n = self.head
            while n:
                print(n.data,'---->',end=" ")
                n = n.ref
    def backward_traversing(self):
        if self.head is None:
            print('cant backward traverse,beacuse its empty')
        else:
            prev = None
            current = self.head 
            while current:
                next = current.ref
                current.ref = prev
                prev = current
                current = next
            self.head = prev
            n = self.head
            while n:
                print(n.data,'------->',end=" ")
                n = n.ref

    def add_begin(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.ref = self.head
            self.head = new_node

    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref:
                n = n.ref
            n.ref = new_node

    def add_before(self,data,x):
        new_node = Node(data)
        if self.head is None:
            print(f'we cant add {data} before {x},becuse its empty list')
        elif self.head.data == x:
            new_node.ref = self.head
            self.head = new_node
        else :
            n = self.head
            found = False
            while n.ref:
                if n.ref.data ==x:
                    found = True
                    break
                n = n.ref
            
            if found:
                new_node.ref = n.ref
                n.ref = new_node
            else:
                print(f'no such node with data {x} in this list')

    
    def add_after(self,data,x):
        new_node = Node(data)
        if self.head is None:
            print(f'we cant add {data} after {x},because its empty')
        elif self.head.data == x:
            if  self.head.ref is None:
              self.head.ref = new_node
            else:
                new_node.ref = self.head.ref
                self.head.ref = new_node
        else:
            n = self.head
            found = False
            while n.ref:
                if n.ref.data == x:
                    found = True
                    break
                n = n.ref
            if found:
                new_node.ref = n.ref.ref
                n.ref.ref = new_node
            else:
                print(f'no such node with data {x} in this list')
    
    def delete_begin(self):
        if self.head is None:
            print('its already empty')
        else:
            self.head = self.head.ref

    def delete_end(self):
        if self.head is None:
            print('its already is empty')
        if self.head is not None and self.head.ref is None:
            self.head = None
        else:
            n = self.head
            while n.ref:
                if n.ref.ref == None:
                    break
                n = n.ref
            n.ref = None

    def delete_by_specified_value(self,x):
        if self.head is None:
            print('its already is empty')
        if self.head.data == x:
            self.head = None
        else:
            n = self.head
            found = False
            while n.ref:
                if n.ref.data ==x:
                    found = True
                    break
                n = n.ref
            if found:
                n.ref = n.ref.ref
            else:
                print(f'{x} not in list')
        
    
    def find_count_sum_avg(self):
        if self.head is None:
            print('cant operate')

        else:
            n = self.head
            sum = 0
            count = 0
            while n:
                sum += n.data
                count +=1
                n = n.ref
            avg = sum/count
            print(sum,count,avg)


     

sll = SLL()
def array_to_linked_list(arr):
    print('1')
    for i in arr:
        print('2')
        sll.add_end(i)
        print('3')

array_to_linked_list([100,200,300])
sll.add_begin(5)
sll.add_begin(4)
sll.add_begin(3)
sll.add_end(6)
sll.add_end(8)
sll.add_before(7,8)
sll.add_after(4.5,4)
sll.delete_begin()
sll.delete_end()
sll.delete_by_specified_value(4.5)
sll.forward_traversing()
print('')
sll.backward_traversing()
sll.find_count_sum_avg()

        
        
        
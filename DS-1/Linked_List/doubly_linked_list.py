class Node:
    def __init__(self,data):
        self.data = data
        self.nref = None
        self.pref = None
class DLL:
    def __init__(self):
        self.head = None
    
    def travers_front(self):
        if self.head is None:
            print('traverse front not possible,its empty')
        else:
            n = self.head
            while n:
                print(n.data,'---->',end=' ')
                n = n.nref
    
    def travers_back(self):
        if self.head is None:
            print('traverse back not possible,its empty')
        else:
            n = self.head
            while n.nref:
                n = n.nref
            
            while n:
                print(n.data,'------->',end=" ")
                n = n.pref

    def insert_empty(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            print('Linked List is not empty')


    def add_begin(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node

    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.nref:
                n = n.nref
            n.nref = new_node
            new_node.pref = n

    def add_before(self,data,x):
        new_node = Node(data)
        if self.head is None:
            print(f'cant add {data} before {x},beacuse its empty')
        elif self.head.data == x:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node
        else:
            n = self.head
            found = False
            while n.nref:
                if n.nref.data == x:
                    found = True
                    break
                n = n.nref
            if found:
                new_node.nref = n.nref
                new_node.pref = n
                n.nref.pref = new_node
                n.nref = new_node
            else:
                print(f'no such node {x} present in this list')

        
    def add_after(self,data,x):
        new_node = Node(data)
        if self.head is None:
             print(f'cant add {data} before {x},beacuse its empty')
        elif self.head.data == x:
            if self.head.nref is None:
                self.head.nref = new_node
                new_node.pref = self.head
            else:
                new_node.nref = self.head.nref
                new_node.pref = self.head
                self.head.nref.pref = new_node
                self.head.nref = new_node
        else:
            n = self.head
            found = False
            while n.nref:
                if n.nref.data == x:
                    found = True
                    break
                n = n.nref
            if found:
                if n.nref.nref:
                    n.nref.nref.pref = new_node
                new_node.nref = n.nref.nref
                new_node.pref = n.nref                
                n.nref.nref = new_node
            else:
                print(f'cant find {x} in list')


    def delete_begin(self):
        if self.head is None:
            print('cant delete from begin ,because its empty')
        else:
            if self.head.nref:
              self.head.nref.pref = None
            self.head = self.head.nref

    def delete_end(self):
        if self.head is None:
            print('cant delete from begin ,because its empty')
        elif self.head.nref is None and self.head is not None:
            self.head = None
        else:
            n = self.head
            while n.nref:
                n = n.nref
            n.pref.nref = None

    
    def delete_by_value(self,x):
        if self.head is None:
            print(f'cant delete {x},beacuse its empty')
        elif self.head.data == x:
            if self.head.nref:
                self.head.nref.pref = None
                self.head = self.head.nref
            else:
                self.head = None

        else:
            n = self.head
            found = False
            while n.nref:
                if n.nref.data == x:
                    found = True
                    break
                n = n.nref
            if found:
                if n.nref.nref:
                    n.nref.nref.pref = n
                    n.nref = n.nref.nref
                else:
                  n.nref = None
            else:
                print(f'{x} not in list')


    def find_sum_count_avg(self):
        if self.head is None:
            print('cant this ,its empty')
        else:
            n = self.head
            sum = 0
            count = 0
            while n:
                sum += n.data
                count += 1
                n = n.nref
            avg = sum/count
            print('sum:',sum,'count:',count,'avg:',avg)






dll = DLL()
def array_to_linked_list(arr):
    for i in arr:
        dll.add_end(i)

dll.add_begin(5)
dll.add_begin(4)
array_to_linked_list([100,200,300])
dll.add_end(6)
dll.add_end(8)
dll.add_before(7,8)
dll.add_after(9,8)
dll.delete_begin()
dll.delete_end()
dll.delete_by_value(7)
dll.travers_front()
print()
dll.travers_back()
print()
dll.find_sum_count_avg()
        


        
        
        
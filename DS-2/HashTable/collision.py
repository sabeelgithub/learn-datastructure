# collision
class HashTable:
    def __init__(self,max):
        self.max = max
        self.arr = [[] for i in range(self.max)]

    
    def getHash(self,key):
        h = 0
        for char in key:
            h += ord(char)
        return h%self.max
    
    def __setitem__(self,key,value):
        h = self.getHash(key)
        found = False
        for idx,element in enumerate(self.arr[h]):
            if len(element)==2 and element[0]==key:
                found = True
                break
        if found:
            self.arr[h][idx] = (key,value)
        else:
            self.arr[h].append((key,value)) 

    def __getitem__(self,key):
        h = self.getHash(key)
        for idx,element in enumerate(self.arr[h]):
            if len(element)==2 and element[0] == key:

                return element[1]
        else:
            return 'no such item here'
        
    def __delitem__(self,key):
        h = self.getHash(key)
        for idx ,element in enumerate(self.arr[h]):
            if len(element)==2 and element[0] == key:
                del self.arr[h][idx]
                return
        else:
           print('no such item in this hash table')
           return 




t = HashTable(5)
t['anshida'] = 200
t['anshida'] = 'love'
t['sabeel'] = 100
print(t['sabeel'])
print(t['sabeels'])
del t['sabeel']
print(t.arr)

        


############################# HASH TABLE #######################



# hash function
def get_hash(key):
        h = 0
        for char in key:
            h += ord(char)
        return h % 10

print(get_hash('sabeel'))
# end


class HashTable:
    def __init__(self):
        self.max = 10
        self.arr = [None for i in range(self.max)]
    
    def get_hash(self,key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.max
    
    def __setitem__(self,key,value):
        h = self.get_hash(key)
        self.arr[h] = value
        return h,self.arr
    
    def __getitem__(self,key):
        h = self.get_hash(key)
        res = self.arr[h]
        return key,res,h
    
    def __delitem__(self,key):
        h = self.get_hash(key)
        self.arr[h] = None
        return self.arr[h],key
        
t = HashTable()
print(t.get_hash('sabeel'))
t['anshida'] = 150
t['sabeel'] = 140
t['molu'] = 130
t['anshidaa'] = 150
print(t['anshida'])
print(t['sabeel'])
print(t['molu'])
print(t['anshidaa'])
del t['molu']
print(t.arr)


# collison

class HashTable:
    def __init__(self):
        self.max = 10
        self.arr = [[] for i in range(self.max)]
    
    def get_hash(self,key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.max
    
    def __setitem__(self,key,value):
        h = self.get_hash(key)
        found = False
        for idx,element in enumerate(self.arr[h]):
            print('h')
            if len(element) == 2 and element[0]==key:
                print('l')
                self.arr[h][idx]=(key,value)
                print('m')
                found = True
                break
        if not found:
               self.arr[h].append((key,value))

        
    
    def __getitem__(self,key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[0],element[1],h
    
    def __delitem__(self,key):
        h = self.get_hash(key)
        for idx,element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][idx]
        
t = HashTable()
print(t.get_hash('sabeel'))

t['anshida'] = 150
t['anshida'] = 170
t['sabeel'] = 140
t['ann'] = 14
t['molu'] = 130
t['anshidaa'] = 'lo'
t['anshida'] = 1000
print(t['anshida'])
print(t['sabeel'])
print(t['molu'])
print(t['anshidaa'])
del t['anshidaa']
print('l',t['anshidaa'])

print(t.arr)




############################## END HASH TABLE ##########################
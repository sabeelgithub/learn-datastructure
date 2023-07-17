
############################# HASH TABLE #######################
def gethash(key):
    h = 0
    for char in key:
        h += ord(char)
    return h % 10

print(gethash('anshida'))

print('----------')

class HashTable:
    def __init__(self,max):
        self.max = max
        self.arr = [None for i in range(self.max)]


    def getHash(self,key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.max
    
    def __setitem__(self,key,value):
        h = self.getHash(key)
        self.arr[h] = value
        return f'item {value} is added at the postion {h} ,the array is {self.arr}'
    
    def __getitem__(self,key):
        h = self.getHash(key)
        return self.arr[h]
    
    def __delitem__(self,key):
        h = self.getHash(key)
        item = self.arr[h]
        self.arr[h] = None
        return f'item {item} is deleted'



t = HashTable(5)
t['anshida'] = 'love'
t['sabeel'] = 100
t['boss'] = 200
print(t['anshida'])
del t['boss']
print(t.arr)

############################## END HASH TABLE ##########################
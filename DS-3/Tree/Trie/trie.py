class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfstring = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def Insert(self,word):
        current = self.root
        for i in word:
            ch = i
            node = current.children.get(ch)
            if node is None:
                node = TrieNode()
                current.children.update({ch:node})
            current = node
        current.endOfstring = True
        return f'item \'{word}\' is added'
    
    def Searching(self,word):
        current = self.root
        for i in word:
            node = current.children.get(i)
            if node is None:
                return False
            current = node
        if current.endOfstring == True:
            return True
        else:
            return False
    


trie = Trie()
print(trie.Insert('sabeel'))
print(trie.Insert('anshida'))
print(trie.Searching('bavu'))
print(trie.root.children)


# creation
# O(1) T
# O(1) S
# insertion
# O(m) T
# O(m) S
# searching
# O(m) T
# O(1) S
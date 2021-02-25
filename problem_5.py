## create a single node in this Trie
class TrieNode:
    def __init__(self):
        self.child_node = {}
        self.node_end = False
    
    def insert(self, char):
        ## insert character in the trie
        self.child_node[char] = TrieNode()
        
    def suffixes(self,suffix=''): 
        # # create empty container to hold suffixes
        suffixes = []
        ## iterate through items of child_node to get char and child node
        for letter, node in self.child_node.items():
            if node.node_end:
                suffixes.append(suffix + letter)
            if node.child_node:
                suffixes += node.suffixes(suffix + letter)
        return suffixes
                
        

class Trie:
    def __init__(self):
        # # get root node 
        self.root_node = TrieNode()

    def insert(self, word):
        # # insert word to the trie
        root = self.root_node
        for letter in word:
            if letter not in root.child_node:
                root.insert(letter)
            root = root.child_node[letter]
        root.node_end = True

    def find(self, prefix):
        # # finding node that contains this prefix and return child node
        root = self.root_node
        for letter in prefix:
            if letter not in root.child_node:
                return []
            root = root.child_node[letter]
        return root



MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)


# In[18]:


from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact
def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')
interact(f,prefix='');








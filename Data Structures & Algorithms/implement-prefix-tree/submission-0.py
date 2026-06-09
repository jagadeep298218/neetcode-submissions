class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.node = TrieNode()

    def insert(self, word: str) -> None:
        root = self.node

        for c in word:
            if c not in root.children:
                root.children[c] = TrieNode()
            root = root.children[c]
        
        root.endOfWord = True

    def search(self, word: str) -> bool:
        root = self.node

        for c in word:
            if c not in root.children:
                return False
            root = root.children[c]

        return root.endOfWord

    def startsWith(self, prefix: str) -> bool:
        root = self.node

        for c in prefix:
            if c not in root.children:
                return False
            root = root.children[c]
        
        return True
        
        
class ListNode:
    def __init__(self, key: int, value: int):
        self.value = value
        self.key = key
        self.left = self.right = None

class LRUCache:
    def __init__(self, capacity: int):
        self.map = {}
        self.cap = capacity
        self.lru = ListNode(0, 0)
        self.mru = ListNode(0, 0)
        self.lru.right = self.mru
        self.mru.left = self.lru
    def delete(self, node):
        node.left.right= node.right
        node.right.left = node.left
    def insert(self, node):
        self.mru.left.right = node
        node.right = self.mru
        node.left = self.mru.left
        self.mru.left= node
    def get(self, key: int) -> int:
        mru, lru = self.mru, self.lru
        
        if key in self.map:
            node= self.map[key]
            self.delete(node)
            self.insert(node)
            return self.map[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.delete(self.map[key])
        self.map[key] = ListNode(key, value)
        self.insert(self.map[key])

        if len(self.map) > self.cap:
            left = self.lru.right
            self.delete(left)
            del self.map[left.key]
    


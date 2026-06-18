class SetUnion:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
    
    def find(self, n):
        p = self.parent[n]
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p
    
    def union(self, n1, n2):
        p1 = self.find(n1)
        p2 = self.find(n2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.parent[p1] = p2
        elif self.rank[p1] < self.rank[p2]:
            self.parent[p2] = p1
        else:
            self.parent[p1] = self.parent[p2]
            self.rank[p1] += 1
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = SetUnion(len(edges) + 1)
        for x, y in edges:
            if not graph.union(x, y):
                return [x, y]




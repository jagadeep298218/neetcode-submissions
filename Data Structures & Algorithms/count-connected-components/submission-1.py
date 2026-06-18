class setUnion:
    def __init__(self, n):
        self.parent = {}
        self.rank = {}
        self.count = n
        for i in range(0, n):
            self.parent[i] = i
            self.rank[i] = 0

    def find(self, n):
        p = self.parent[n]
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p
    
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)

        if p1 == p2:
            return 
        if self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
            self.count -= 1
        elif self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
            self.count -= 1
        else:
            self.parent[p2] = p1
            self.count -= 1
            self.rank[p1] += 1
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = setUnion(n)

        for x, y in edges:
            graph.union(x, y)
        
        return graph.count
    
            

        
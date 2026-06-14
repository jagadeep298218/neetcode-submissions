class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        vertices = {i : [] for i in range(n)}
        count = 0
        for i, j in edges:
            vertices[i].append(j)
            vertices[j].append(i)
        
        seen = set()

        def dfs(vertice, parent):
            if vertice in seen:
                return 
            seen.add(vertice)
            for v in vertices[vertice]:
                if v == parent:
                    continue
                dfs(v, vertice)
        
        for v in range(n):
            l = len(seen)
            dfs(v, v-1)
            if l < len(seen):
                count += 1
        
        return count
                

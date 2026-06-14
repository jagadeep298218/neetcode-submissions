class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # no cycles and E = V - 1
        # undirected graph
        if len(edges) != n - 1:
            return False
        adj_list = {i : [] for i in range(n)}

        for i, j in edges:
            adj_list[i].append(j)
            adj_list[j].append(i)

        seen = set()

        def dfs(vertice, parent):
            if vertice in seen:
                return False
            seen.add(vertice)
            for v in adj_list[vertice]:
                if v == parent:
                    continue
                if not dfs(v, vertice):
                    return False
            
            adj_list[vertice] = []
            return True

        return dfs(0, -1) and len(seen) == n

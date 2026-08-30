class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        out = {}
        inc = {}
        for ai, bi in trust:
            out[bi] = out.get(bi, 0) + 1
            inc[ai] = inc.get(ai, 0) + 1
        
        for p in out:
            if out[p] == n-1 and inc.get(p, 0) == 0:
                return p

        return -1

            
class Solution:
    def firstUniqChar(self, s: str) -> int:
        check = set()
        c = []
        for char in s:
            if char in check:
                if char in c:
                    c.remove(char)
            else:
                c.append(char)
                check.add(char)
        if len(c) > 0:
            return s.index(c[0])
        else: return -1
                
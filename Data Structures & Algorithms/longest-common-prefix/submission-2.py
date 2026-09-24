class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        least = 0
        for s in strs:
            if len(s) < len(strs[least]):
                least = strs.index(s)
        master = list(strs[least])

        for s in strs:
            if len(s) == 0:
                return ""
            for char in range(min(len(s), len(master))):
                if master[char] == s[char]:
                    continue
                else:
                    master = master[0:char]
                    break
        return "".join(master)

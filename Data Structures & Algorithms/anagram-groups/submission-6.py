class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        keys = {}
        check = [0] * 26
        for word in strs:
            for letter in word:
                check[ord(letter) - 97] += 1
            key = tuple(check)
            keys[key] = keys.get(key, [])
            keys[key].append(word)
            check = [0] * 26

        res = []
        for key in keys:
            res.append(keys[key])
        return res

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        master = defaultdict(list)
        for word in strs:
            temp = [0] * 26
            for char in word:
                temp[ord(char)-ord('a')] += 1
            master[tuple(temp)].append(word)

        return list(master.values())
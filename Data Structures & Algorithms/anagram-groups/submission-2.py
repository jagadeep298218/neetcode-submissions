class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_list = {}
        final = []

        for i in range(len(strs)):
            sorted_text = sorted(strs[i])
            y = "".join(sorted_text)

            if y in anagram_list:
                anagram_list[y].append(strs[i])

            else:
                anagram_list[y] = [strs[i]]
        
        for i in anagram_list:
            val = anagram_list.get(i, 0)
            final.append(val)
        
        return final



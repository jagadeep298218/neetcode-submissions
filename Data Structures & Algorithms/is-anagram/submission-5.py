class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = [0] * 26
        t_list = [0] * 26

        for i in s:
            s_list[ord(i) - ord("a")] += 1

        for j in t:
            t_list[ord(j) - ord("a")] += 1

        return s_list == t_list


        
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        baskets = {}
        left = 0
        res = 0
        for right in range(len(fruits)):
            baskets[fruits[right]] = baskets.get(fruits[right], 0) + 1
            while len(baskets) > 2:
                baskets[fruits[left]] -= 1
                if baskets[fruits[left]] == 0:
                    del baskets[(fruits[left])]
                left += 1
            
            res = max(res, right-left+1)

        return res
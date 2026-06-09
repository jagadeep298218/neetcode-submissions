class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(x, k):
            c = 0
            for pile in x:
                c += math.ceil(pile / k)
            return c 

        piles.sort()

        left, right = 1, piles[-1]

        while left <= right:
            mid = (right + left) // 2
            count = check(piles, mid)

            if count <= h:
                right = mid - 1
                res = mid
            else:
                left = mid + 1
            
        return res
            


        
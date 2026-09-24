class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        find min eating rate
        start with  for
        pile1 /rate1 + pile2/rate2 + .. = h
        sort array
        try with mid then half and check where h lands
        '''
        def eat(rate, arr):
            global res
            res = 0
            for ele in arr:
                res += (ele + rate - 1)//rate
            return res

        left = 1
        right = max(piles)
        final = float("inf")
        while left <= right:
            mid = (left + right)//2
            res = eat(mid, piles)
            if res <= h:
                right = mid - 1
                final = mid
            else: 
                left = mid + 1

        return final



        
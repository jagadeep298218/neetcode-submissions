import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        choose_gifts = []
        for i in gifts:
            choose_gifts.append(-i)
        heapq.heapify(choose_gifts)
        res = 0

        for i in range(0, k):
            num = heapq.heappop(choose_gifts)
            pos = -1 * num
            sqrt = floor(math.sqrt(pos))
            heapq.heappush(choose_gifts, -sqrt)

        for i in range(len(gifts)):
            pos = -1 * heapq.heappop(choose_gifts)
            res+= pos
        return res
            


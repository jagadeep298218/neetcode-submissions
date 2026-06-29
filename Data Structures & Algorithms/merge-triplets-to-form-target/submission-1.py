class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = []
        for triplet in triplets:
            if triplet[0] <= target[0] and triplet[1] <= target[1] and triplet[2] <= target[2]:
                res.append(triplet)
        
        for i in range(1, len(res)):
            a, b, c = res[i-1][0], res[i-1][1], res[i-1][2]
            x, y, z = res[i][0], res[i][1], res[i][2]

            res[i] = [max(a, x), max(b, y), max(c, z)]
        if not res:
            return False
        return res[-1] == target
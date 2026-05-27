class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = []
        count = {}

        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i], 0) + 1

        for num, cnt in count.items():
            bucket.append([cnt, num])
        bucket.sort()

        result = []

        while len(result) < k:
            result.append(bucket.pop()[1])
        return result
                
            

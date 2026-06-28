class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = []
        for i in range(len(gas)):
            diff.append(gas[i]-cost[i])
        
        def check(length, index, gas):
            while length < len(diff):
                gas += diff[index]
                if gas < 0:
                    return -1
                if index == len(diff)-1:
                    index = 0
                else:
                    index +=1
                length += 1
            return index
            
        for i in range(len(diff)):
            if diff[i] >= 0:
                if check(0, i, 0) > -1:
                    return i
        
        return -1
            
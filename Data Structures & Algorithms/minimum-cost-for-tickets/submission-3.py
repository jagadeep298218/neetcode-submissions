class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        '''track of -> days valid, index
        function: return the min total cost. states: days,index
        base: if index not in range --> return 0
        recur:
        return min of costs[0] + (1, index+1), costs[1] + (7, index+1), costs[2] + (30, index+1)'''

        def dp(valid, index):
            if index >= len(days): 
                return 0
            if valid > days[index]:
                memo[(valid, index)] = dp(valid, index+1)
            if (valid, index) in memo:
                return memo[(valid, index)]
            else: 
                memo[(valid, index)] = min(costs[0] + dp(days[index] +1, index+1), costs[1] + dp(days[index]+7, index+1), costs[2] + dp(days[index]+30, index+1))
            return memo[(valid, index)]

        memo = {}
        return dp(0, 0)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) ==1:
            return 0 
        
        buy, sell = 0, 1
        max_profit = 0
        while (buy < sell) and (sell < len(prices)):
            profit = prices[sell] - prices[buy]
            max_profit = max(profit, max_profit)
            if prices[buy] > prices[sell]:
                buy = sell
                sell+=1
            else:
                sell+=1
        return max_profit


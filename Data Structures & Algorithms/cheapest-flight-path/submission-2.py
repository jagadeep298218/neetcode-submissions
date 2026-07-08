class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k+1):
            tmpPrices = prices.copy()

            for source, dest, cost in flights:
                if prices[source] == float("inf"):
                    continue
                if prices[source] + cost < tmpPrices[dest]:
                    tmpPrices[dest] = prices[source] + cost
            prices = tmpPrices
        return -1 if prices[dst] == float("inf") else prices[dst]
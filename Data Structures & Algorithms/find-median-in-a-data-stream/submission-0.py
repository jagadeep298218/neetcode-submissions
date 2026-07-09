class MedianFinder:
    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
    def addNum(self, num: int) -> None:
        minHeap, maxHeap = self.minHeap, self.maxHeap
        if minHeap and num > minHeap[0]:
            heapq.heappush(minHeap, num)
        else:
            heapq.heappush(maxHeap, -num)
        if len(minHeap) > len(maxHeap) + 1:
            val = heapq.heappop(minHeap)
            heapq.heappush(maxHeap, -val)
        if len(maxHeap) > len(minHeap) + 1:
            val = heapq.heappop(maxHeap)
            heapq.heappush(minHeap, -val)

    def findMedian(self) -> float:
        minHeap, maxHeap = self.minHeap, self.maxHeap
        if len(minHeap) == len(maxHeap):
            return float(-maxHeap[0] + (minHeap[0]))/2
        if len(minHeap) > len(maxHeap):
            return float(minHeap[0])
        else:
            return float(-maxHeap[0])
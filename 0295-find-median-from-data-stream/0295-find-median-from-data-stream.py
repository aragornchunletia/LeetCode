from heapq import heappop , heappush
"""
using 2 heaps
bottom half a maxHeap
Top half a minHeap
always keeping len(bottom) > len(top) for stream break at odd number elements
return bottom[0]
else return avg(bottom[0] + top[0])
"""
class MedianFinder:

    def __init__(self):
        self.bottom = []
        self.top = []

        

    def addNum(self, num: int) -> None:
        heappush(self.bottom , -num)
        heappush(self.top , -heappop(self.bottom))
        if len(self.bottom) < len(self.top):
            heappush(self.bottom , -heappop(self.top))



    def findMedian(self) -> float:
        if len(self.bottom) != len(self.top):
            return -self.bottom[0]
        else:
            return (self.top[0] - self.bottom[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
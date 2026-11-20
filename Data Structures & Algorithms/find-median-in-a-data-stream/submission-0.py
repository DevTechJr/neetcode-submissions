import heapq


class MedianFinder:

    def __init__(self):
        # Max-heap (store negated values) for the lower half
        self.small: list[int] = []
        # Min-heap for the upper half
        self.large: list[int] = []

    def addNum(self, num: int) -> None:
        # 1. Push to max-heap, then move its largest element to min-heap
        heapq.heappush(self.small, -num)
        heapq.heappush(self.large, -heapq.heappop(self.small))

        # 2. Rebalance so lower half has equal or one more element than upper half
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2.0
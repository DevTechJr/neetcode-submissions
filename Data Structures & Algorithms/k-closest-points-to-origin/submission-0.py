class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = [(x*x+y*y,x,y) for x,y in points]
        heapq.heapify(min_heap)
        res = []
        for time in range(k):
            dist, x, y = heapq.heappop(min_heap)
            res.append([x,y])
        print(res)
        return res
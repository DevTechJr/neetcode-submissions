class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adj = {i:[] for i in range(1, n+1)}

        for u,v,t in times:
            adj[u].append((t,v))
        
        minHeap = [(0,k)]
        visited = set()
        min_time = 0

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visited:
                continue
            visited.add(n1)
            min_time = max(min_time, w1)

            for w2, n2 in adj[n1]:
                if n2 not in visited:
                    heapq.heappush(minHeap, (w1+w2, n2))
        
        return min_time if len(visited) == n else -1
        
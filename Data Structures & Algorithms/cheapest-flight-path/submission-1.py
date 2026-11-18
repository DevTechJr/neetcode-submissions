class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for u,v, price in flights:
            graph[u].append((v,price))
        
        min_stops = [float("inf")] * n
        pq = [(0, src, 0)]
        while pq:
            cost,city, stops = heapq.heappop(pq)
            

            if city == dst:
                return cost
            
            if stops > k or stops >= min_stops[city]:
                continue
            
            min_stops[city] = stops
            
            for neigh, price in graph[city]:
                heapq.heappush(pq, ((cost + price), neigh, stops+1))
        return -1
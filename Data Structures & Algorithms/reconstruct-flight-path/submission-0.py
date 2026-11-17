class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {}
        
        # 1. Build adjacency list
        for from_, to_ in tickets:
            if from_ not in adj:
                adj[from_] = []
            adj[from_].append(to_)
        
        # 2. Sort destinations alphabetically so we always pick the smallest lexical order first
        for airport in adj:
            adj[airport].sort()
            
        result = []
        
        # 3. Post-order DFS (Hierholzer's Algorithm)
        def dfs(airport):
            # While this airport still has outgoing flights...
            while adj.get(airport):
                # Pop the first (lexicographically smallest) destination
                next_destination = adj[airport].pop(0)
                dfs(next_destination)
            
            # When we hit a dead end, add the airport to our result 
            # (it gets added in reverse order of completion)
            result.append(airport)

        # 4. Always start our journey at "JFK"
        dfs("JFK")
        
        # 5. Reverse the result because we recorded it from the end backwards
        return result[::-1]
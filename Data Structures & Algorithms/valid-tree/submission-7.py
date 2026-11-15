from collections import deque

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adj = {i: [] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u) # FIX 1: Uncommented and fixed to append u!

        visited = set()
        q = deque()

        q.append((0, -1))
        visited.add(0) # FIX 2: Mark visited IMMEDIATELY upon pushing

        while q:
            node, parent = q.popleft()

            for neigh in adj[node]:
                if neigh == parent:
                    continue
                if neigh in visited:
                    return False  # Hit an already visited node that isn't our parent -> CYCLE!
                
                visited.add(neigh)  # Mark visited IMMEDIATELY upon pushing
                q.append((neigh, node))

        return len(visited) == n
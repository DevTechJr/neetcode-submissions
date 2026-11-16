class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parents = list(range(n + 1))

        # Recursive find with path compression
        def find(node):
            if parents[node] == node:
                return node
            parents[node] = find(parents[node])  # Flattens the tree
            return parents[node]

        def union(u, v):
            root_u = find(u)
            root_v = find(v)

            if root_u != root_v:
                parents[root_v] = root_u  # Attach root_v under root_u
                return True
            else:
                return False  # Same root! Cycle detected.

        for u, v in edges:
            if not union(u, v):
                return [u, v]
                
        return []
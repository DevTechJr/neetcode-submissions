"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # print(node.val)
        # print(len(node.neighbors))
        old_to_new = {}
        def clone(node):
            if node is None:
                return

            if node in old_to_new:
                return old_to_new[node]

            new_node = Node()
            new_node.val = node.val
            old_to_new[node] = new_node
            
            for n in node.neighbors:
                new_node.neighbors.append(clone(n))
                print(f"current node is {new_node.val} and neighbor is {n.val}")

            return new_node
        

        new_node = clone(node)
        return new_node
    

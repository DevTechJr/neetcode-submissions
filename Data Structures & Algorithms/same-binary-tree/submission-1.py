# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        
        def traverse(node_p, node_q):
            if node_p is None and node_q is None:
                return True

            if node_p is None or node_q is None or node_p.val != node_q.val:
                return False

            return traverse(node_p.left, node_q.left) and traverse(node_p.right, node_q.right)
        
        return traverse(p, q)
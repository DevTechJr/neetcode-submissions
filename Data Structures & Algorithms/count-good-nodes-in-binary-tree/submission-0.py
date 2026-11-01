# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        counter = 0
        def traverse(node, max_sf):
            nonlocal counter

            if (node.val >= max_sf):
                counter += 1
            
            max_sf = max(max_sf, node.val)

            if node.left is not None:
                traverse(node.left, max_sf)
            if node.right is not None:
                traverse(node.right, max_sf)
            
        traverse(root, root.val)
        return counter

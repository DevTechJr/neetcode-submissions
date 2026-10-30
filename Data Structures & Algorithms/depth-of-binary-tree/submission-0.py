# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        counter = 0
        if root is None:
            return 0
         # recursively count depth
        def traverse(node):
            if node.left != None and node.right != None:
                return 1 + max(traverse(node.left), traverse(node.right))
            elif node.left != None and node.right == None:
                return 1 + traverse(node.left)
            elif node.left == None and node.right != None:
                return 1+ traverse(node.right)
            return 1


        result = traverse(root)
        return result
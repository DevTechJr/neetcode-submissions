# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diamater = 0
        def traverse(node):
            nonlocal diamater

            if node is None:
                return 0

            left_height = traverse(node.left)
            right_height = traverse(node.right)

            diamater = max(diamater, left_height + right_height)

            return 1 + max(left_height, right_height)
        

        traverse(root)
        return diamater
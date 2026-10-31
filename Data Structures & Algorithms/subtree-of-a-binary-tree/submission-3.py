# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        
        def match(node, subRoot):
            if subRoot is None and node is None:
                return True
            if subRoot is None or node is None or subRoot.val != node.val:
                return False
            return match(node.left, subRoot.left) and match(node.right, subRoot.right)
            
                
        def traverse(node, subRoot):
            if node is None and subRoot is None:
                return True
            if node is None:
                return False

            if (node.val == subRoot.val) and match(node, subRoot):
                return True
            return traverse(node.left, subRoot) or traverse(node.right, subRoot)
            
            
        
        return traverse(root, subRoot)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        
        def switch(node):
            if node.left is not None or node.right is not None:
                    tempLeft = node.left
                    node.left = node.right
                    node.right = tempLeft
                    if node.left != None:
                        switch(node.left)
                    
                    if node.right != None:
                        switch(node.right)
                    
                    return
        
        switch(root)
        return root


        

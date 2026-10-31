class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Base case: if root is null, or we found p or q
        if not root or root == p or root == q:
            return root
        
        # Look for p and q in the left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # If both left and right are non-null, p and q are in separate subtrees -> current root is LCA
        if left and right:
            return root
        
        # Otherwise, return the non-null child (or None if neither found)
        return left if left else right
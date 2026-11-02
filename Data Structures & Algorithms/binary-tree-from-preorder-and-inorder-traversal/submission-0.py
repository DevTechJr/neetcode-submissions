class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # A hash map to instantly find a value's index in 'inorder' (Hint 4!)
        inorder_map = {val: i for i, val in enumerate(inorder)}
        
        pre_idx = 0
        
        def helper(in_left, in_right):
            nonlocal pre_idx
            
            # Base case: if there are no elements to construct, return None
            if in_left > in_right:
                return None
                
            # 1. Grab the current root value from preorder and advance the pointer
            root_val = preorder[pre_idx]
            pre_idx += 1
            root = TreeNode(root_val)
            
            # 2. Find where this root is located in the inorder array (O(1) time using our map!)
            idx = inorder_map[root_val]
            
            # 3. Recursively build the left and right subtrees
            # Everything to the left of 'idx' goes to the left subtree
            root.left = helper(in_left, idx - 1)
            # Everything to the right of 'idx' goes to the right subtree
            root.right = helper(idx + 1, in_right)
            
            return root
            
        return helper(0, len(inorder) - 1)
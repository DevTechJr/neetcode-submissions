# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        results = []
        q = deque()
        if root is None:
            return []
        q.append(root)
        while len(q) >0:
            len_size = len(q)
            for i in range(len(q)):
                temp_node = q.popleft()
                if i == len_size-1:
                    results.append(temp_node.val)
                if temp_node.left is not None:
                    q.append(temp_node.left)
                if temp_node.right is not None:
                    q.append(temp_node.right)
        return results

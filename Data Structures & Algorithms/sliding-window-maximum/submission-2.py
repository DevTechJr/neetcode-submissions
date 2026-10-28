from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()  # stores indices of elements in the current window
        
        for i in range(len(nums)):
            # 1. Remove indices that are out of the current window bounds
            if q and q[0] < i - k + 1:
                q.popleft()
            
            # 2. Remove elements from the back of the queue that are smaller than the current element
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            
            # 3. Add the current element's index
            q.append(i)
            
            # 4. Once we've hit the size of the first window, record the max (front of queue)
            if i >= k - 1:
                res.append(nums[q[0]])
                
        return res
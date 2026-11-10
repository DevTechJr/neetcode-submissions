class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        max_so_far = nums[0]
        min_so_far = nums[0]
        result = nums[0]
        
        for i in range(1, len(nums)):
            curr = nums[i]
            
            # Since a negative number flips min and max, 
            # we compute candidates using curr, curr * max_so_far, and curr * min_so_far
            temp_max = max(curr, max_so_far * curr, min_so_far * curr)
            min_so_far = min(curr, max_so_far * curr, min_so_far * curr)
            
            max_so_far = temp_max
            
            # Update the global maximum found so far
            result = max(result, max_so_far)
            
        return result
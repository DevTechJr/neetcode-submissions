class Solution:
    def rob(self, nums: List[int]) -> int:

        memo = {}
        
        def climb(i):
            
            if i > len(nums)-1:
                return 0
            
            if i in memo:
                return memo[i]
            
            memo[i] = nums[i] + max(climb(i+2), climb(i+3))
            return memo[i]
        
        return max(climb(0), climb(1))
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        
        # If the total sum is odd, it's mathematically impossible to split into two equal integers
        if total_sum % 2 != 0:
            return False
            
        target = total_sum // 2
        
        # dp[i] will be True if we can form a subset sum equal to i
        dp = [False] * (target + 1)
        dp[0] = True  # Base case: a sum of 0 is always possible (by picking nothing)
        
        for num in nums:
            # Go backwards from target down to num to avoid using the same number twice
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]
                
        return dp[target]
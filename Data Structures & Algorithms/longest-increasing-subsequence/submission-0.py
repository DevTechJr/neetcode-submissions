class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # track min seen so far and length
        
        if not nums:
            return 0
        
        cost = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    cost[i] = max(cost[i], cost[j]+1)
        
        return max(cost)
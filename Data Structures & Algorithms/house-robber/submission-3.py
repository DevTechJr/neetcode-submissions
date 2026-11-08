class Solution:
    def rob(self, nums: List[int]) -> int:

        nums_len = len(nums)

        cost = [0] * (nums_len+1)

        if nums_len <= 2:
            return max(nums)

        cost[0] = nums[0]
        cost[1] = max(nums[1], nums[0])

        for house in range(2, nums_len):
            cost[house] = max(nums[house] + cost[house-2], cost[house-1])
        
        return max(cost[nums_len-1], cost[nums_len-2])

        # memo = {}
        
        # def climb(i):
            
        #     if i > len(nums)-1:
        #         return 0
            
        #     if i in memo:
        #         return memo[i]
            
        #     memo[i] = max(nums[i] + climb(i+2), climb(i+1))
        #     return memo[i]
        
        # return climb(0)
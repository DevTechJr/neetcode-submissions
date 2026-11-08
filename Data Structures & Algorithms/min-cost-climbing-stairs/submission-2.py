class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost_len = len(cost)
        nums = [0] * (cost_len + 1)

        nums[0] = cost[0]
        nums[1] = cost[1]

        for step in range(2, cost_len):
            nums[step] = cost[step] + min(nums[step-1], nums[step-2])
        
        return min(nums[cost_len-1], nums[cost_len-2])

                

        # memo = {}

        # def climb(i):
        #     if i >= len(cost):
        #         return 0
            
        #     if i in memo:
        #         return memo[i]
            
        #     memo[i] = cost[i] + min(climb(i+1), climb(i+2))
        #     return memo[i]
        
        # return min(climb(0), climb(1))
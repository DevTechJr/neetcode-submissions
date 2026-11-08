class Solution:
    def climbStairs(self, n: int) -> int:
        
        nums = [0] * (n+1)

        nums[0] = 1
        nums[1] = 1


        for step in range(2, n+1):
            nums[step] = nums[step-1] + nums[step-2]
        
        return nums[n]


        # memo = [None] * 80

        # def climb(step):
        #     if step == 1:
        #         return 1
        #     if step == 2:
        #         return 2
            
        #     if memo[step]:
        #         return memo[step]
            
        #     memo[step] = climb(step-1) + climb(step-2)
        #     return memo[step]

        
        # return climb(n)

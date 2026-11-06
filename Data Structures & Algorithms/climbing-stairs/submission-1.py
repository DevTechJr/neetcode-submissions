class Solution:
    def climbStairs(self, n: int) -> int:
        
        memo = [None] * 80

        def climb(step):
            if step == 1:
                return 1
            if step == 2:
                return 2
            
            if memo[step]:
                return memo[step]
            
            memo[step] = climb(step-1) + climb(step-2)
            return memo[step]

        
        return climb(n)

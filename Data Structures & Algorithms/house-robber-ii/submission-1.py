class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) <= 3:
            return max(nums)

        def helper(sub_nums):
            memo = {}
            
            def climb(i):
                if i > len(sub_nums)-1:
                    return 0
                
                if i in memo:
                    return memo[i]
                
                memo[i] = sub_nums[i] + max(climb(i+2), climb(i+3))
                return memo[i]

            
            return max(climb(0), climb(1))
        
        return max(helper(nums[1:]), helper(nums[:-1]))
        
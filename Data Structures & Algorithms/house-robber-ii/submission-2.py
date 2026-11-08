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
                
                memo[i] = max(sub_nums[i] + climb(i+2), climb(i+1))
                return memo[i]

            
            return climb(0)
        
        return max(helper(nums[1:]), helper(nums[:-1]))
        
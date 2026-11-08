class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        def helper(sub_nums: list[int]) -> int:
            length = len(sub_nums)
            if length == 1:
                return sub_nums[0]
            
            # Allocate an array of exact length
            cost = [0] * length
            cost[0] = sub_nums[0]
            cost[1] = max(sub_nums[0], sub_nums[1])
            
            for i in range(2, length):
                cost[i] = max(sub_nums[i] + cost[i-2], cost[i-1])
                
            return cost[length - 1]

        # Circular check: max of (excluding last house, excluding first house)
        return max(helper(nums[:-1]), helper(nums[1:]))
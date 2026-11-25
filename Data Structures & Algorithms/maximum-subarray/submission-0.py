class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        temp_sum = nums[0]

        for ind in range(1, len(nums)):
            temp_sum = max(nums[ind], nums[ind]+temp_sum)
            max_sum = max(temp_sum, max_sum)
        return max_sum

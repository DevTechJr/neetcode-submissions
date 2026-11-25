class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxSum = nums[0]
        for step in range(1, len(nums)):
            maxSum -= 1
            if maxSum < 0:
                return False
            maxSum = max(maxSum, nums[step])
            if maxSum == 0 and nums[step] == 0:
                if step == len(nums)-1:
                    return True
                else:
                    return False
        return True
            

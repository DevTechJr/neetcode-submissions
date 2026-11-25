class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums)-1

        for ind in range(len(nums)-1, -1,-1 ):
            if ind + nums[ind] >= goal:
                goal = ind

        return True if goal == 0 else False
            

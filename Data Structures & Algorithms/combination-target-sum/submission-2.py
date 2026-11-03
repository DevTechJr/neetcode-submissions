class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []
        path = []

        def backtrack(i):
            curr_sum = sum(path)
            if curr_sum == target:
                results.append(path.copy())
                return
            
            if curr_sum > target or i == len(nums):
                return
            
            path.append(nums[i])
            backtrack(i)
            path.pop()
            backtrack(i+1)
        
        backtrack(0)
        return results
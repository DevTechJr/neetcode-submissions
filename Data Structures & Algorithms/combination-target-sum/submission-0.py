class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []
        path = []

        def backtrack(i):
            if sum(path) == target:
                results.append(path.copy())
                return
            
            if sum(path) > target or i == len(nums):
                return
            
            path.append(nums[i])
            backtrack(i)
            path.pop()
            backtrack(i+1)
        
        backtrack(0)
        return results
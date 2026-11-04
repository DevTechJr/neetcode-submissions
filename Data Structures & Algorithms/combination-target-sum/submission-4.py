class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []

        def backtrack(i, path):
            if sum(path) == target:
                results.append(path[:])
                return
            
            if sum(path) > target:
                return

            for ix in range(i, len(nums)):
                path.append(nums[ix])
                backtrack(ix, path)
                path.pop()
        
        backtrack(0, [])
        return results
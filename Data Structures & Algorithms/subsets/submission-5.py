class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []

        def backtrack(i, path):
            
            results.append(path[:])
            
            for ix in range(i, len(nums)):
                path.append(nums[ix])
                backtrack(ix+1, path)
                path.pop()
                

        backtrack(0, [])
        print(results)
        return results
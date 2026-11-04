class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        perm = []


        def backtrack(perm):
            if len(perm) == len(nums):
                results.append(perm.copy())
                return

            for i in range(len(nums)):
                if nums[i] in perm:
                    continue
                perm.append(nums[i])
                backtrack(perm)
                perm.pop()

        
        backtrack([])
        print(results)
        return results
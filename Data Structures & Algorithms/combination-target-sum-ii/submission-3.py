class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        results = []
        
        def backtrack(start: int, target: int, path: List[int]):
            if target == 0:
                results.append(path.copy())
                return
            
            for i in range(start, len(candidates)):
                # Skip duplicates at the same recursion level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                # Since the array is sorted, if the current number exceeds target, 
                # all subsequent numbers will too.
                if candidates[i] > target:
                    break
                
                path.append(candidates[i])
                backtrack(i + 1, target - candidates[i], path)
                path.pop()
                
        backtrack(0, target, [])
        return results
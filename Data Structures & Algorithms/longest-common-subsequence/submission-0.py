class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache = {}
        count = 0

        def dfs(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            
            if (i, j) in cache:
                return cache[(i,j)]
            
            if text1[i] == text2[j]:
                ans = 1 + dfs(1+i, 1+j)
            else:
                ans = max(dfs(1+i, j), dfs(i, j+1))
            
            cache[(i,j)] = ans
            return ans
        
        return dfs(0,0)


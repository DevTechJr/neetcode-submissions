class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        cache = {}

        def dfs(i: int, j: int) -> bool:
            if i == len(s1) and j == len(s2):
                return True
            if (i, j) in cache:
                return cache[(i, j)]

            k = i + j
            ans = False

            if i < len(s1) and s1[i] == s3[k] and dfs(i + 1, j):
                ans = True
            elif j < len(s2) and s2[j] == s3[k] and dfs(i, j + 1):
                ans = True

            cache[(i, j)] = ans
            return ans

        return dfs(0, 0)
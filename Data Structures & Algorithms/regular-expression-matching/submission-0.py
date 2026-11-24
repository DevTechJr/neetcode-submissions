class Solution:

  def isMatch(self, s: str, p: str) -> bool:
    cache = {}

    def dfs(i: int, j: int) -> bool:
      if (i, j) in cache:
        return cache[(i, j)]

      if j == len(p):
        return i == len(s)

      matched = i < len(s) and (s[i] == p[j] or p[j] == ".")

      # Handle "x*" or ".*"
      if j + 1 < len(p) and p[j + 1] == "*":
        # 0 occurrences of p[j] + '*' OR 1+ occurrences if current char matches
        ans = dfs(i, j + 2) or (matched and dfs(i + 1, j))
      else:
        ans = matched and dfs(i + 1, j + 1)

      cache[(i, j)] = ans
      return ans

    return dfs(0, 0)
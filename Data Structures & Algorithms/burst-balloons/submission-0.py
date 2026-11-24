from typing import List


class Solution:

  def maxCoins(self, nums: List[int]) -> int:
    # Pad both ends with 1 so out-of-bounds neighbors multiply by 1
    nums = [1] + nums + [1]
    memo = {}

    def dfs(l: int, r: int) -> int:
      # No balloons left in this range
      if l > r:
        return 0
      if (l, r) in memo:
        return memo[(l, r)]

      best = 0
      # Try every balloon i in [l, r] as the LAST balloon to burst
      for i in range(l, r + 1):
        coins = nums[l - 1] * nums[i] * nums[r + 1]
        coins += dfs(l, i - 1) + dfs(i + 1, r)
        best = max(best, coins)

      memo[(l, r)] = best
      return best

    # Solve for the original array range (indices 1 through len(nums) - 2)
    return dfs(1, len(nums) - 2)
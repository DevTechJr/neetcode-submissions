class Solution:

  def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
    results = set()  # Use a set to automatically handle duplicates
    nums.sort()  # Sort to ensure identical subsets match
    path = []

    def backtrack(i):
      # Base case: reached the end of the array
      if i >= len(nums):
        results.add(tuple(path))  # Convert list to tuple so it can go in a set
        return

      # Choice 1: Include nums[i]
      path.append(nums[i])
      backtrack(i + 1)
      path.pop()  # Backtrack

      # Choice 2: Exclude nums[i]
      backtrack(i + 1)

    backtrack(0)
    # Convert the set of tuples back to a list of lists
    return [list(t) for t in results]
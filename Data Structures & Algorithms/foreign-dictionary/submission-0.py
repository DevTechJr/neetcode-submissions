import collections
from typing import List


class Solution:

  def foreignDictionary(self, words: List[str]) -> str:
    # Step 1: Initialize graph and in-degree map for all unique characters
    adj = {char: set() for word in words for char in word}
    in_degree = {char: 0 for char in adj}

    # Step 2: Build the graph by comparing adjacent words
    for i in range(len(words) - 1):
      w1, w2 = words[i], words[i + 1]
      min_len = min(len(w1), len(w2))

      # Invalid prefix case: e.g., ["abc", "ab"]
      if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
        return ""

      for j in range(min_len):
        if w1[j] != w2[j]:
          # If edge doesn't already exist, add it and increment in-degree
          if w2[j] not in adj[w1[j]]:
            adj[w1[j]].add(w2[j])
            in_degree[w2[j]] += 1
          break  # Only the first differing character matters

    # Step 3: Initialize queue with all nodes having 0 in-degree
    queue = collections.deque([char for char in in_degree if in_degree[char] == 0])
    res = []

    # Step 4: Process the queue (BFS topological sort)
    while queue:
      char = queue.popleft()
      res.append(char)

      for neighbor in adj[char]:
        in_degree[neighbor] -= 1
        if in_degree[neighbor] == 0:
          queue.append(neighbor)

    # Step 5: If result length doesn't cover all unique chars, a cycle exists
    if len(res) < len(adj):
      return ""

    return "".join(res)
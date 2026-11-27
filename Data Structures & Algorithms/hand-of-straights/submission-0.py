import heapq
from typing import List


class Solution:

  def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
    if len(hand) % groupSize:
      return False

    count = {}
    for n in hand:
      count[n] = count.get(n, 0) + 1

    minH = list(count.keys())
    heapq.heapify(minH)

    while minH:
      # Skip numbers already exhausted by earlier groups
      while minH and count[minH[0]] == 0:
        heapq.heappop(minH)
      if not minH:
        break

      first = minH[0]
      for i in range(first, first + groupSize):
        if count.get(i, 0) == 0:
          return False

        count[i] -= 1
        if count[i] == 0:
          # If i isn't the current minimum, a smaller number still needs i later
          if i != minH[0]:
            return False
          heapq.heappop(minH)

    return True
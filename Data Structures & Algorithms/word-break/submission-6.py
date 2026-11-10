class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cost = [False] * (len(s) + 1)
        cost[0] = True
        
        # Outer loop: Go through every index from left to right
        for ind in range(len(s)):
            if not cost[ind]:
                continue
            
            # Inner loop: Test ALL words at this current reachable index
            for word in wordDict:
                if s.startswith(word, ind):
                    cost[ind + len(word)] = True
                    
        return cost[len(s)]
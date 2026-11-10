class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        s_len = len(s)
        memo = {}
        def climb(start_idx):
            if start_idx == s_len:
                return True
            
            if start_idx in memo:
                return memo[start_idx]
            
            for word in wordDict:
                if s.startswith(word, start_idx):
                    if climb(start_idx + len(word)):
                        memo[start_idx] = True
                        return True
        
            memo[start_idx] = False
            return memo[start_idx]

        return climb(0)
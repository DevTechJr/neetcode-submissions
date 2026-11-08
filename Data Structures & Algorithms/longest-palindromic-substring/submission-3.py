class Solution:
    def longestPalindrome(self, s: str) -> str:
        best = ''

        if len(s) == 1:
            return s[0]
        
        for i in range(len(s)):
            # even palindromes:
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > len(best):
                    best = s[l:r+1]
                l-=1
                r+=1
            
            # odd palindromes:
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > len(best):
                    best = s[l:r+1]
                l-=1
                r+=1

        return best
class Solution:
    def countSubstrings(self, s: str) -> int:
        memo = []

        for x in range(len(s)):
            # even palindromes
            l, r = x, x+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                memo.append(s[l:r+1])
                l-=1
                r+=1
            # odd palindromes           
            l, r = x, x
            while l >= 0 and r < len(s) and s[l] == s[r]:
                memo.append(s[l:r+1])
                l -= 1
                r += 1
        return len(memo)


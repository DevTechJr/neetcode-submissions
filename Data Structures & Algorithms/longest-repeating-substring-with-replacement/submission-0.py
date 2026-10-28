class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        myChar = {}
        left = 0
        res = 0
        max_len = 0
        most_freq = 0

        for i in range(len(s)):
            myChar[s[i]] = myChar.get(s[i],0)+1

            # find most freq value within the window
            most_freq = max(most_freq, myChar[s[i]])
            window_len = i-left+1

            # Use while to keep shrinking until window is valid
            while window_len - most_freq > k:
                myChar[s[left]] -= 1
                left += 1
                window_len = i - left + 1  # Recalculate window length after shrinking
            max_len = max(max_len, window_len)

        return max_len
        
        
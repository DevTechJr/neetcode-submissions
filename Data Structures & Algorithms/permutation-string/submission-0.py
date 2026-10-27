class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        myChar = {}
        tempChar = {}
        # left, right starts at 0
        # if letter is not in s1 dict, continue
        # else and count of letter = 0, left = current and track the letter
        # if (nested) all values are 1, return true
        for char in s1:
            myChar[char] = myChar.get(char, 0) + 1
        
        for i in range(len(s1)):
            tempChar[s2[i]] = tempChar.get(s2[i], 0) + 1

        left = 0
        for right in range((len(s1)),len(s2)):
            if tempChar == myChar:
                return True
            
            tempChar[s2[right]] = tempChar.get(s2[right], 0) + 1

            tempChar[s2[left]] -= 1
            if tempChar[s2[left]] == 0:
                del tempChar[s2[left]]
            left+=1
        return myChar == tempChar
            

            

            
        
        
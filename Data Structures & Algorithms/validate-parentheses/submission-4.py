class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        key_dict = {"[":"]", "{":"}", "(":")"}
        for char in s:
            if char in ['[', '(', '{']:
                stack.append(char)
            elif len(stack) == 0 and char in [']', ')', '}']:
                    return False
            elif char in [']', ')', '}']:
                result = stack.pop()
                if key_dict[result] != char:
                    return False 
        if len(stack) != 0:
            return False
        else:
            return True
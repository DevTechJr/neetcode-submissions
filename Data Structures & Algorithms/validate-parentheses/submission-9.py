class Solution:
    def isValid(self, s: str) -> bool:
        myStack = []
        # Mapping closing brackets to their corresponding opening brackets
        myRef = {
            "}": "{",
            "]": "[",
            ")": "("
        }
        
        for char in s:
            if char in myRef.values():
                # If it's an opening bracket, push it to the stack
                myStack.append(char)
            elif char in myRef.keys():
                # If it's a closing bracket:
                # 1. Check if stack is empty (prevents IndexError)
                # 2. Check if the popped opening bracket matches the expected one
                if not myStack or myStack.pop() != myRef[char]:
                    return False
                    
        # Return True only if all opening brackets were matched and popped
        return not myStack
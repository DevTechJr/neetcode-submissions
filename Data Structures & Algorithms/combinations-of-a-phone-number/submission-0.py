class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []
        
        numMap = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }

        results = []

        def backtrack(index, path):



            if index == len(digits):
                tem = "".join(path[:])
                results.append(tem)
                return
            
            
            temp = numMap[digits[index]]
            for num in temp:
                path.append(num)
                backtrack(index+1, path)
                path.pop()
                

                
            
        backtrack(0, [])
        print(results)
        return results
            
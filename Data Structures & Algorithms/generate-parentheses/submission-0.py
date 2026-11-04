class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []

        def backtrack(string, open_c, close_c):
            if len(string) == 2*n:
                results.append(string)
                return
            
            if open_c < n:
                backtrack(string + "(", open_c + 1, close_c)
            
            if close_c < open_c:
                backtrack(string + ")", open_c, close_c + 1)

            
        backtrack("", 0, 0)
        print(results)
        return results
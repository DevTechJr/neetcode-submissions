class Solution:
    def partition(self, s: str) -> List[List[str]]:

        results = []
       

        def backtrack(index, path):
            if index == len(s):
                results.append(path[:])
                return
            
            for end in range(index, len(s)):
                substring = s[index:end+1]
                if substring == substring[::-1]:
                    path.append(substring)
                    backtrack(end+1, path)
                    path.pop()
            
        backtrack(0, [])
        return results

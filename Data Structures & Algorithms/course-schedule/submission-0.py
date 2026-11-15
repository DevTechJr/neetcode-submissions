class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = {i:[] for i in range(numCourses)}
        for u,v in prerequisites:
            adj_list[u].append(v)
        
        state = [0] * numCourses

        def dfs(course):
            if state[course] == 1:
                return False
            if state[course] == 2:
                return True
            
            state[course] = 1

            for neigh in adj_list[course]:
                result = dfs(neigh)
                if result == False:
                    return False
            
            state[course] = 2
            return True

        for course in range(numCourses):
            result = dfs(course)
            if result == False:
                return False
        return True
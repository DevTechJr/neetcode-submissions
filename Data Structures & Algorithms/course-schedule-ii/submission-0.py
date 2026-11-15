from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i:[] for i in range(numCourses)}
        deps = [0] * numCourses
        for course, pre in prerequisites:
            adj[pre].append(course)
            deps[course] += 1
        
        q = deque()

        for course in range(numCourses):
            if deps[course] == 0:
                q.append(course)
        
        results = []

        while q and len(q) >0:
            course = q.popleft()
            results.append(course)
            for neigh in adj[course]:
                deps[neigh] -= 1
                if deps[neigh] == 0:
                    q.append(neigh)
        
        if len(results) == numCourses:
            return results
        else:
            return []

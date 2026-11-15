from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i:[] for i in range(numCourses)}
        deps = [0] * numCourses

        for course, pre in prerequisites:
            adj[pre].append(course)
            deps[course] += 1
        q = deque()
        for item in range(numCourses):
            if deps[item] == 0:
                q.append(item)
        
        # now do bfs
        comp_count = 0
        while q and len(q) > 0:
            course = q.popleft()
            comp_count += 1
            for neigh in adj[course]:
                deps[neigh] -= 1
                if deps[neigh] == 0:
                    q.append(neigh)
        
        return comp_count == numCourses


        
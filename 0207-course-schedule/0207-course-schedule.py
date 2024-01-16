class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseReqs = {}

        for i in range(numCourses):
            courseReqs[i] = []
        
        for c, r in prerequisites:
            courseReqs[c].append(r)

        visited = set() # all courses along the current DFS path

        def dfs(course):
            if course in visited:
                return False

            if courseReqs[course] == []:
                return True

            visited.add(course)

            for req in courseReqs[course]:
                if not dfs(req):
                    return False
                
            visited.remove(course)
            courseReqs[course] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True
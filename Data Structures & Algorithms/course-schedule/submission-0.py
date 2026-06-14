class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_map = {i : [] for i in range(numCourses) }

        for c, p in prerequisites:
            course_map[c].append(p)
        
        seen = set()
        def dfs(c):
            if c in seen:
                return False
            if course_map[c] == []:
                return True
            seen.add(c)
            for crs in course_map[c]:
                if not dfs(crs):
                    return False
            seen.remove(c)
            course_map[c] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course_map = {i: [] for i in range(numCourses)}
        for c, p in prerequisites:
            course_map[c].append(p)

        res = []
        seen = set()    
        done = set()     
        def dfs(c):
            if c in seen:    
                return False
            if c in done:     
                return True

            seen.add(c)
            for pre in course_map[c]:
                if not dfs(pre):
                    return False
            seen.remove(c)

            done.add(c)
            res.append(c)     
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []
        return res
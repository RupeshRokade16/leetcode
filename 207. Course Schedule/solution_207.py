class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Find cyclic relation in the course-prereq

        For 1, we store 2, 3, 4 (if those were prereqs)
        Now we know for sure that,
        for course 2, 3, 4, we cant have 1 in it else we return False

        for every course, start consuming the prereqs in a dfs manner
        """
        courseMapping = defaultdict(set)
        res = True

        def dfs(course, path):
            prereqs = courseMapping[course]
            nonlocal res

            if not prereqs:
                return True
            
            if course in path:
                res = False
                return

            path.add(course)
            for prereq in prereqs:
                dfs(prereq, path)
            path.remove(course)


        for course, prereq in prerequisites:
            courseMapping[course].add(prereq)
            
            #Early check
            if course in courseMapping[prereq]:
                return False
        
        for obj in courseMapping.items():
            print(obj)
            dfs(obj[0], set())


        return res

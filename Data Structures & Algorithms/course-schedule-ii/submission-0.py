class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i : [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        output = []
        cycle = set()
        visiting = set()

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visiting:
                return True
                
            cycle.add(crs)
            for pre in preMap[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)
            visiting.add(crs)
            output.append(crs)
            return True
        for i in range(numCourses):
            if dfs(i) == False:
                return []

        return output

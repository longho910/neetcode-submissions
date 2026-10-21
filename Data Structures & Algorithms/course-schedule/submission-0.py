class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = { i : [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visiting = set()
        def dfs(crs):
            if crs in visiting:
                return False
            if preMap[crs] == []:
                return True
            visiting.add(crs)
            for pre in preMap[crs]:
                if dfs(pre) == False:
                    return False
            preMap[crs] = []
            visiting.remove(crs)
            return True
        for i in range(numCourses):
            if dfs(i) == False:
                return False 
        return True
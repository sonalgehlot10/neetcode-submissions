class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i:[] for i in range(numCourses)}
        visiting = set()
        visited = set()
        res = []
        
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        def dfs(crs):
            if crs in visiting:
                return False
            if crs in visited:
                return True
            # if preMap[crs] == []:
            #     return True

            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            preMap[crs] = []
            res.append(crs)
            visited.add(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return res
class Solution(object):
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        def floydWarshall(reachable):
            for k in range(numCourses):
                for i in range(numCourses):
                    for j in range(numCourses):
                        reachable[i][j] = reachable[i][j] or (reachable[i][k] and reachable[k][j])
            
            return reachable
            
        
        adjMatrix =  [[ 0 for i in range(numCourses)] for j in range(numCourses)]
        for i in prerequisites:
            adjMatrix[i[0]][i[1]] = 1
        
        #print(adjMatrix)
        ans = []
        floydWarshall(adjMatrix)
        #print(adjMatrix)
        for i in queries:
            ans.append(bool(adjMatrix[i[0]][i[1]]))
        
        return ans
        
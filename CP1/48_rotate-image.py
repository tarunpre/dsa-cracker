class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        #transpose
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        #reflect
        for row in matrix:
            n = len(row)
            for i in range(n//2):
                row[i], row[n-i-1]  = row[n-i-1], row[i]
        
        
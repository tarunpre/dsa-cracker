class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        top = 0
        left = 0
        right = len(matrix[0])
        bottom = len(matrix)
        mt = []
        while top < bottom and left < right:

            for i in range(left, right):
                mt.append(matrix[top][i])
            top += 1

            for i in range(top,bottom):
                mt.append(matrix[i][right-1])
            right -= 1
            
            if not (top < bottom and left < right):
                break

            for  i in range(right-1,left-1,-1):
                mt.append(matrix[bottom-1][i])
            bottom -= 1

            for i in range(bottom-1, top-1, -1):
                mt.append(matrix[i][left])
            left += 1

        return mt
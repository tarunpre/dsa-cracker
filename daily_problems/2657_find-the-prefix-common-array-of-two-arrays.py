class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        ck = []
        for i in range(len(A)):
            c= 0
            if A[i] == B[i]:
                c += 1
            else:
                if A[i] in B[:i+1]:
                    c+= 1
                if B[i] in A[:i+1]:
                    c += 1
            if ck:
                c += ck[-1]
            ck.append(c)
        return ck
        
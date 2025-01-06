class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        ln = len(boxes)
        k = [0] * ln
        for m in range(ln):
            if boxes[m] == "1":
                for np in range(ln):
                    k[np] += abs(np - m)
        return k

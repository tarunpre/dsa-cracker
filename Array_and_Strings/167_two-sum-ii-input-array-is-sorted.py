class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        k = {}
        for i in range(len(numbers)):
            dff = target - numbers[i]
            if numbers[i] in k:
                return [k[numbers[i]]+1,i+1]
            else:
                k[dff] = i        
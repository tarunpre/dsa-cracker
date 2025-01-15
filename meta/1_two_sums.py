class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dc = {}
        for i in range(len(nums)):
            diff = target-nums[i]
            if diff in dc:
                return [i,dc[diff]]
            else:
                dc[nums[i]] = i
        
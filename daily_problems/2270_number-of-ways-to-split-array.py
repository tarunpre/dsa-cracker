from typing import List
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        presum = []
        p = 0
        for x in nums:
            p += x
            presum.append(p)
        o = 0
        for i in range(len(presum)-1):
            if presum[i] >= presum[-1] - presum[i]:
                o += 1
        return o

# T = O(n)
# S = O(n)
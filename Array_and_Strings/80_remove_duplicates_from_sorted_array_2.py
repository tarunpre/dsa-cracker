# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii

from typing import List



class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ln = len(nums)
        if ln < 3:
            return ln
        j = 2
        for i in range(2, ln):
            if nums[i] != nums[j-2]:
                nums[j] = nums[i]
                j += 1
        assert j == 5
        return j
    
#solution 1
#Time complexity: O(N)
#Space complexity O(1)    
sol = Solution()
sol.removeDuplicates([1,1,1,2,2,3])
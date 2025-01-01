# https://leetcode.com/problems/remove-element

from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #solution 1
        #Time complexity: O(N)
        #Space complexity O(1)
        j = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        return j
        #solution 2
        #Time complexity: O(N)
        #Space complexity O(1)
        '''
        while val in nums:
            nums.remove(val)
        '''
sol = Solution()
assert 2 == sol.removeElement([3,2,2,3], 3)
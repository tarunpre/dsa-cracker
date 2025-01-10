# https://leetcode.com/problems/rotate-array

from typing import List



class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ln = len(nums)
        if k > ln:
            k = k % ln
        nums.reverse()
        nums[:k], nums[k:] = nums[:k][::-1], nums[k:][::-1]
        # nums[:k], nums[k:] = reversed(nums[:k]), reversed(nums[k:])
        # nums[:] = nums[-k:] + nums[:-k]
        assert nums == [5,6,7,1,2,3,4]
        

#solution 1
#Time complexity: O(N)
#Space complexity O(1)    
   
sol = Solution()
sol.rotate([1,2,3,4,5,6,7], 3)
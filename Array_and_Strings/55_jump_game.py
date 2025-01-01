# https://leetcode.com/problems/jump-game

from typing import List



class Solution:
    def canJump(self, nums: List[int]) -> bool:
        ln = len(nums)
        if ln == 1:
            return True
        j = ln-1
        for i in range(ln-2, -1,-1):
            if i+nums[i] >= j:
                j = i
        assert j ==0
        if j == 0:
            return True
        return False
    
       
#solution 1
#Time complexity: O(N)
#Space complexity O(1)    
sol = Solution()
sol.canJump([2,3,1,1,4])
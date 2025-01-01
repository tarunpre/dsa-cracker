# https://leetcode.com/problems/majority-element

from typing import List



class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''
        nums.sort()
        i = len(nums) // 2
        return nums[i]
        '''
        res = 0
        count = 0
        for n in nums:
            if not count:
                res = n
            if res == n:
                count += 1
            else:
                count -= 1
        assert 2==res
        return res

#solution 1
#Time complexity: O(NLogN)
#Space complexity O(1)    

#solution 2 = Boyer-Moore Voting Algorithm
#Time complexity: O(N)
#Space complexity O(1)   
sol = Solution()
sol.majorityElement([2,2,1,1,1,2,2])
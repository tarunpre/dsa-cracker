from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sub = 2
        if sum(nums) == target:
            return len(nums)
        for x in nums:
            if x >= target:
                return 1
        r = 0
        l = 0
        sm = float("inf")
        while l < len(nums)-1:
            if sum(nums[l:r]) >= target:
                sm = min(sm,len(nums[l:r]))
                l += 1
            else:
                r += 1
        return sm

sol = Solution()
sol.minSubArrayLen(7, [2,3,1,2,4,3])
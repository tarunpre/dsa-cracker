from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        w = 0
        l = 0
        r = 1
        c = 0
        for r in range(1, len(height)):
            if height[l] < height[r]:
                c = 0
                l = r
            else:
                c += 1
                w = max(w,c * height[r])
        return w
sol = Solution()
sol.maxArea([1,8,6,2,5,4,8,3,7])    
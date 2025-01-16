class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        num = None
        for x in nums2:
            if num == None:
                num = x
            else:
                num = num ^ x
        m = None
        for j in nums1:
            if len(nums2) % 2 == 0:
                if m == None:
                    m = 0 ^ num
                else:
                    m = m ^ 0 ^ num
            else:
                if m == None:
                    m = j ^ num
                else:
                    m = m ^ j ^ num
        return m
    
#T = O(m+n)
#S = O(1)
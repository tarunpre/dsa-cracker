# https://leetcode.com/problems/merge-sorted-array

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #solution 1
        #Time complexity: O(NLogN)
        #Space complexity O(1)
        '''
        del nums1[m:]
        nums1.extend(nums2)
        nums1.sort()
        '''

        #solution 2
        #Time complexity: O(m+n)
        #Space complexity O(1)
        n1 = m-1
        n2 = n-1
        for i in range(m+n-1,-1,-1):
            #checking array out of index
            if n1 < 0:
                nums1[i] = nums2[n2]
                n2 -= 1
            #checking array out of index
            elif n2 < 0:
                nums1[i] = nums1[n1]
                n1 -= 1
            #replacing bigger value
            else:
                if nums1[n1] < nums2[n2]:
                    nums1[i] = nums2[n2]
                    n2 -= 1
                else:
                    nums1[i] = nums1[n1]
                    n1 -= 1
        assert nums1 == [1,2,2,3,5,6]

sol = Solution()
sol.merge([1,2,3,0,0,0], 3, [2,5,6], 3)
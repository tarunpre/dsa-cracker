# https://leetcode.com/problems/best-time-to-buy-and-sell-stock

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = 0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                p += prices[i]-prices[i-1]
        assert 7 == p
        return p
        '''
                p = 0
        m = prices[0]
        for i in range(len(prices)):
            if prices[i] < m:
                m = prices[i]
            else:
                p += prices[i]-m
                m = prices[i]
        return p
        '''
    
#solution 1,2
#Time complexity: O(N)
#Space complexity O(1)    
sol = Solution()
sol.maxProfit([7,1,5,3,6,4])
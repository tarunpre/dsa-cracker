# https://leetcode.com/problems/best-time-to-buy-and-sell-stock

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = 0
        m = prices[-1]
        for i in range(len(prices)-1, -1, -1):
            if prices[i] > m:
                m = prices[i]
            if m - prices[i] > p:
                p = m-prices[i]
        assert 5 == p
        return p


    
#solution 1
#Time complexity: O(N)
#Space complexity O(1)    
sol = Solution()
sol.maxProfit([7,1,5,3,6,4])
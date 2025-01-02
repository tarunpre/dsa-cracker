# https://leetcode.com/problems/maximum-score-after-splitting-a-string

class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        zero = 0
        mx = 0
        ones = s.count('1')
        for i in range(len(s)-1):
            if s[i] == '0':
                zero += 1
            else:
                ones -= 1
            mx = max(mx, zero+ones)
        return mx
    
# T = O(n)
# S = O(1)


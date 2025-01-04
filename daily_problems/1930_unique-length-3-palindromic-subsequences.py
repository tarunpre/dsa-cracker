class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        for i in set(s):
            fi = s.index(i)
            ri = s.rindex(i)
            if fi < ri:
                result += len(set(s[fi+1:ri]))
        return result    


# T = O(26N) = O(N)
# S = O(1)
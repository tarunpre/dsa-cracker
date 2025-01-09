class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s:
            return True
        if len(s) > len(t):
            return False
        j = 0
        for i in range(len(t)):
            if t[i] == s[j]:
                j += 1
                if j == len(s):
                    return True
        return False

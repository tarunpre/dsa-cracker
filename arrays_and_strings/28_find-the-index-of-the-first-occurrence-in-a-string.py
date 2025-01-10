class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(haystack) < len(needle):
            return -1
        for i in range(len(haystack)):
            if needle == haystack[i:i+len(needle)]:
                return i
        return -1
        
# T = O(N)
# S = O(1)
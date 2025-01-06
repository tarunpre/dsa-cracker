class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        dic = {}
        for r in ransomNote:
            if r in dic:
                dic[r] += 1
            else:
                dic[r] = 1
        for k, v in dic.items():
            if magazine.count(k) < v:
                return False
        return True